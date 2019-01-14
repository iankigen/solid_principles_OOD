"""
Interface segregation principle states that many specialized interfaces are better than one universal. In other words
we can say this also that client must not be forced to implement an interface that it doesn’t use. So the main purpose
is to divide the interfaces so that they are more specific.
"""

# BAD PRACTICE

from abc import ABCMeta, abstractmethod
import time

print('>' * 10)
print('BAD')
print('>' * 10)


class AbstractWorker(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Worker(AbstractWorker):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(AbstractWorker):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Manager(object):

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, AbstractWorker), "`worker` must be of type {}".format(AbstractWorker)

        self.worker = worker

    def manage(self):
        self.worker.work()

    def lunch_break(self):
        self.worker.eat()


# Implement the `Robot` class. However, due to the api defined by `AbstractWorker`,
# we have to reimplement `eat` method which is not necessary for a `Robot`.

class Robot(AbstractWorker):

    def work(self):
        print("I'm a robot. I'm working....")

    def eat(self):
        print("I don't need to eat....")  # This code doing nothing but it is a must. (Bad!)


def main():
    manager = Manager()
    manager.set_worker(Worker())
    # Make normal worker works.
    manager.manage()
    # lunch break
    manager.lunch_break()

    # super worker
    manager.set_worker(SuperWorker())
    manager.manage()
    manager.lunch_break()

    manager.set_worker(Robot())
    manager.manage()
    # However, a robot can eat.....
    manager.lunch_break()


main()

# GOOD PRACTICE
print('>' * 10)
print('GOOD')
print('>' * 10)


class Workable(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def work(self):
        pass


class Eatable(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def eat(self):
        pass


class AbstractWorker(Workable, Eatable):
    pass


class Worker(AbstractWorker):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(AbstractWorker):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Manager(object):

    def __init__(self):
        self.worker = None


class WorkManager(Manager):

    def set_worker(self, worker):
        assert isinstance(worker, Workable), "`worker` must be of type {}".format(Workable)

        self.worker = worker

    def manage(self):
        self.worker.work()


class BreakManager(Manager):

    def set_worker(self, worker):
        assert isinstance(worker, Eatable), "`worker` must be of type {}".format(Eatable)
        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


class Robot(Workable):

    def work(self):
        print("I'm a robot. I'm working....")

    # No need for implementation of `eat` which is not neccessary for a `Robot`.


def main():
    work_manager = WorkManager()
    break_manager = BreakManager()
    work_manager.set_worker(Worker())
    break_manager.set_worker(Worker())
    # Make normal worker works.
    work_manager.manage()
    # lunch break
    break_manager.lunch_break()

    # super worker
    work_manager.set_worker(SuperWorker())
    break_manager.set_worker(SuperWorker())
    work_manager.manage()
    break_manager.lunch_break()

    work_manager.set_worker(Robot())
    work_manager.manage()
    try:
        break_manager.set_worker(Robot())
        break_manager.lunch_break()
    except:
        pass


main()
