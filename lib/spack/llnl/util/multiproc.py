# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

"""
This implements a parallel map operation but it can accept more values
than multiprocessing.Pool.apply() can.  For example, apply() will fail
to pickle functions if they're passed indirectly as parameters.
"""
from multiprocessing import Process, Semaphore, Value
from multiprocessing.pool import Pool

__all__ = ["Barrier", "NoDaemonPool"]


class Barrier:
    """Simple reusable semaphore barrier.

    Python 2 doesn't have multiprocessing barriers so we implement this.

    See https://greenteapress.com/semaphores/LittleBookOfSemaphores.pdf, p. 41.
    """

    def __init__(self, n, timeout=None):
        self.n = n
        self.to = timeout
        self.count = Value("i", 0)
        self.mutex = Semaphore(1)
        self.turnstile1 = Semaphore(0)
        self.turnstile2 = Semaphore(1)

    def wait(self):
        if not self.mutex.acquire(timeout=self.to):
            raise BarrierTimeoutError()
        self.count.value += 1
        if self.count.value == self.n:
            if not self.turnstile2.acquire(timeout=self.to):
                raise BarrierTimeoutError()
            self.turnstile1.release()
        self.mutex.release()

        if not self.turnstile1.acquire(timeout=self.to):
            raise BarrierTimeoutError()
        self.turnstile1.release()

        if not self.mutex.acquire(timeout=self.to):
            raise BarrierTimeoutError()
        self.count.value -= 1
        if self.count.value == 0:
            if not self.turnstile1.acquire(timeout=self.to):
                raise BarrierTimeoutError()
            self.turnstile2.release()
        self.mutex.release()

        if not self.turnstile2.acquire(timeout=self.to):
            raise BarrierTimeoutError()
        self.turnstile2.release()


class BarrierTimeoutError(Exception):
    pass


class NoDaemonProcess(Process):
    """Daemon processes are not allowed to create child processes.
    Yet most meaningful funciontality in spack requires system-interaction via
    child processes."""
    # make 'daemon' attribute always return False
    def _get_daemon(self):
        return False

    def _set_daemon(self, value):
        pass

    daemon = property(_get_daemon, _set_daemon)


# We sub-class multiprocessing.pool.Pool instead of multiprocessing.Pool
# because the latter is only a wrapper function, not a proper class.
class NoDaemonPool(Pool):
    """Daemon processes are not allowed to create child processes.
    Yet most meaningful funciontality in spack requires system-interaction via
    child processes."""
    Process = NoDaemonProcess
