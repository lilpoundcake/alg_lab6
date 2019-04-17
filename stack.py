#!/usr/bin/env python
# -*- coding: utf-8 -*-


class StackOverflowError(RuntimeError):
    pass


class StackIsEmptyError(RuntimeError):
    pass


class Stack:
    def __init__(self, size):
        self.size = size
        self.storage = [0] * size
        self.head = -1

    def push(self, v):
        if self.head == self.size - 1:
            raise StackOverflowError()
        elif self.head < self.size - 1:
            self.head += 1
            self.storage[self.head] = v

    def pop(self):
        if self.head == -1:
            raise StackIsEmptyError()
        else:
            return self.storage[self.head]
            self.storage[self.head] = 0
            self.head -= 1

    def __len__(self):
        return self.head + 1

"""stack = Stack(1)
print(stack.__len__())
stack.push(12)
try:
    stack.push(12)
except StackOverflowError:
    print('StackOverflowError')
print(stack.__len__())
stack.pop()
stack.pop()
print(stack.__len__())"""