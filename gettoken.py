#!/usr/bin/env python
def get_value(*args):
    return "Hello World " + ":".join(map(str, args))
