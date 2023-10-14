#!/usr/bin/python3
'''
Module: '0-minoperations'
Function that returns min number of minimum operations for a task
'''


def minOperations(n):
    '''Returns int(min number of operations)'''
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
