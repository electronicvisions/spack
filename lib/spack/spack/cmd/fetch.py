# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import llnl.util.tty as tty

import spack.cmd
import spack.cmd.common.arguments as arguments
import spack.config
import spack.environment as ev
import spack.repo

description = "fetch archives for packages"
section = "build"
level = "long"


def setup_parser(subparser):
    arguments.add_common_arguments(subparser, ["no_checksum", "deprecated"])
    subparser.add_argument(
        "-m",
        "--missing",
        action="store_true",
        help="fetch only missing (not yet installed) dependencies",
    )
    subparser.add_argument(
        "-D", "--dependencies", action="store_true", help="also fetch all dependencies"
    )
    # begin VISIONS (added)
    subparser.add_argument(
        '-f', '--file', action='append', default=[],
        dest='specfiles', metavar='SPEC_YAML_FILE',
        help="fetch from file. Read specs to fetch from .yaml files")
    # end VISIONS
    arguments.add_common_arguments(subparser, ["specs"])
    subparser.epilog = (
        "With an active environment, the specs "
        "parameter can be omitted. In this case all (uninstalled"
        ", in case of --missing) specs from the environment are fetched"
    )


def fetch(parser, args):
    # begin VISIONS (added)
    specs = []
    # end VISIONS
    if args.specs:
    # begin VISIONS (modified)
        specs += spack.cmd.parse_specs(args.specs, concretize=True)
    if args.specfiles:
        for specfile in args.specfiles:
            with open(specfile, 'r') as f:
                s = spack.spec.Spec.from_yaml(f)

            if s.concretized().dag_hash() != s.dag_hash():
                msg = 'skipped invalid file "{0}". '
                msg += 'The file does not contain a concrete spec.'
                tty.warn(msg.format(file))
                continue

            specs.append(s.concretized())
    if not (args.specs or args.specfiles):
    # end VISIONS
        # No specs were given explicitly, check if we are in an
        # environment. If yes, check the missing argument, if yes
        # fetch all uninstalled specs from it otherwise fetch all.
        # If we are also not in an environment, complain to the
        # user that we don't know what to do.
        env = ev.active_environment()
        if env:
            if args.missing:
                specs = env.uninstalled_specs()
            else:
                specs = env.all_specs()
            if specs == []:
                tty.die(
                    "No uninstalled specs in environment. Did you " "run `spack concretize` yet?"
                )
        else:
            # begin VISIONS (modified)
            tty.die("fetch requires at least one package argument or specfile")
            # end VISIONS

    if args.no_checksum:
        spack.config.set("config:checksum", False, scope="command_line")

    if args.deprecated:
        spack.config.set("config:deprecated", True, scope="command_line")

    for spec in specs:
        if args.missing or args.dependencies:
            for s in spec.traverse(root=False):
                # Skip already-installed packages with --missing
                if args.missing and s.installed:
                    continue

                s.package.do_fetch()
        spec.package.do_fetch()
