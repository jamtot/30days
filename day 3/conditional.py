#!/bin/python3

import math
import os
import random
import re
import sys

def weird(n):
    if n % 2 == 1 or (n > 5 and n < 21):
        print("Weird")
    else:
        print("Not Weird")

if __name__ == '__main__':
    N = int(input())
    weird(N)
