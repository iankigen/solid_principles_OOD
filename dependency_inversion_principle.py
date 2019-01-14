"""
High level modules should not depend on low-level modules, both should depend on abstractions and Abstractions should
not depend on details. Details should depend on abstractions.
"""

# BAD PRACTICE
print('>' * 10)
print('BAD PRACTICE')
print('>' * 10)
from abc import ABCMeta, abstractmethod


class Worker(object):

    def work(self):
        print("I'm working!!")


class Manager(object):

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, Worker), '`worker` must be of type {}'.format(Worker)

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


class SuperWorker(object):

    def work(self):
        print("I work very hard!!!")


# Now you can see what happens if we want the `Manager` to support `SuperWorker`.
#  1. The `set_worker` must be modified or it will not pass the type-checking.
#  2. The `manage` method should be re-test, which means you may or may not have to
#     rewrite the testing code.

def main():
    worker = Worker()
    manager = Manager()
    manager.set_worker(worker)
    manager.manage()

    # The following will not work...
    super_worker = SuperWorker()
    try:
        manager.set_worker(super_worker)
    except AssertionError:
        print("manager fails to support super_worker....")


main()

# GOOD PRACTICE
# Here we solve the issues in the design in `BAD PRACTICE` with an interface (implemented with abstract class).

print('>' * 10)
print('GOOD PRACTICE')
print('>' * 10)


class IWorker(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def work(self):
        pass


# `IWorker` defines a interface which requires `work` method.

class Worker(IWorker):

    def work(self):
        print("I'm working!!")


class Manager(object):

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, IWorker), '`worker` must be of type {}'.format(Worker)

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()
            # And some complex codes go here....


class SuperWorker(IWorker):

    def work(self):
        print("I work very hard!!!")


# Now, the manager support `SuperWorker`...
# In addition, it will support any worker which obeys the interface defined by `IWorker`!

def main():
    worker = Worker()
    manager = Manager()
    manager.set_worker(worker)
    manager.manage()

    # The following will not work...
    super_worker = SuperWorker()
    try:
        manager.set_worker(super_worker)
        manager.manage()
    except AssertionError:
        print("manager fails to support super_worker....")


if __name__ == "__main__":
    main()
