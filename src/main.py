#!/usr/bin/env python3

import sys


class Adder():
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def getSum(self):
        return self.val1 + self.val2


if __name__ == "__main__":
    print("Starting program")

    adder = Adder(sys.argv[1], sys.argv[2])
    print(adder.getSum())

    print("Done with program")
