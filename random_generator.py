from random import random

__author__ = 'vladimir'


from posix import urandom
from binascii import hexlify
from numpy import mean, std, var


def generate_random_num():
    """
    Random num generator based on bytes from /dev/urandom.
    :return:
    """
    return (long(hexlify(urandom(7)), 16) >> 3) * 2**(-53)


class RandomAnalyze(object):
    def __init__(self, count):
        self.numbers = [generate_random_num() for x in xrange(count)]

    def variance(self):
        return var(self.numbers)

    def standard_deviation(self):
        return std(self.numbers)


test = RandomAnalyze(700)
print 'Variance ' + str(test.variance())
print 'Standard deviation ' + str(test.standard_deviation())
