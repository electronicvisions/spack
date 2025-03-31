- note that you have to build on a machine whose instruction set is
  common to all machines the software will be used on.  in our case
  that likely is one of the older cluster nodes, i.e. AMTHostN.
  (passing `-march` and `-mtune` flags did not work reliably)

- always (!) set your umask first:
  ```
  umask 0002
  ```

- set up the repository
  ```
  git init --shared=all
  git remote add origin https://github.com/electronicvisions/spack
  git checkout origin/visionary
  git submodule update --init
  ```

- unload any modules you may have loaded:
  ```
  module purge
  ```

- load the spack commands:
  ```
  source share/spack/setup-env.sh
  ```

- install a newer compiler:
  ```
  spack fetch --dependencies gcc@7.2.0
  srun --pty --mem 14G -N1 -c8 -p compile -t 8:00:00 spack install gcc@7.2.0 %gcc@4.9.2
  ```

- activate compiler:
  ```
  spack compiler find --scope site opt/spack/linux-debian8-x86_64/gcc-4.9.2/gcc-7.2.0-*
  ```

- install visionary-defaults:
  ```
  spack fetch --dependencies visionary-defaults+tensorflow
  srun --pty --mem 14G -N1 -c8 -p compile -t 8:00:00 spack install visionary-defaults~tensorflow
  ```

- install visionary-defaults+tensorflow (i.e. compile tensorflow on frontend):
  ```
  spack install -j3 visionary-defaults+tensorflow
  ```

- Create a filesystem view:
  ```
  spack view -dependencies yes hardlink -i spackview visionary-defaults+tensorflow
  spack view -dependencies no hardlink -i spackview gcc@7.2.0
  ```

- Make the view world-readable (because e.g. jenkins is not a member of the F9 group)
  ```
  chmod -R o+rX spackview opt
  ```

- Optional: To generate an image (speeds up access via NFS) file:
  ```
  dd if=/dev/zero of=spackview.img bs=1 count=0 seek=12G
  mkfs.ext2 spackview.img
  mkdir image_tmp
  mount spackview.img image_tmp
  cp -a spackview/* image_tmp/
  cp -a spackview/.[a-z]* image_tmp/
  umount image_tmp
  rmdir image_tmp
  ```
