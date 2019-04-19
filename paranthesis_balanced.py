#!/usr/bin/env python
# -*- coding: utf-8 -*-

class StackOverflowError(RuntimeError):
    pass


class StackIsEmptyError(RuntimeError):
    pass


class Stack:
    def __init__(self, size):
        self.size = size
        self.storage = [None] * size
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
            out_num = self.storage[self.head]
            self.storage[self.head] = None
            self.head -= 1
            return out_num

    def __len__(self):
        return self.head + 1

def is_paranthesis_balanced(s):
    parathesis = Stack(len(s))
    for i in range(len(s)):
        if s[i] in '([{<':
            parathesis.push(s[i])
        elif s[i] in ')]}>':
            if parathesis.__len__() == 0:
                return False
            else:
                out_num = parathesis.pop()
                if out_num == '[' and s[i] == ']':
                    continue
                elif out_num == '(' and s[i] == ')':
                    continue
                elif out_num == '{' and s[i] == '}':
                    continue
                elif out_num == '<' and s[i] == '>':
                    continue
                else:
                    return False
    if parathesis.__len__() == 0:
        return True
    