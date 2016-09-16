#!/usr/bin/env python
import os


def simple_test():
    here = os.path.dirname(os.path.realpath(__file__))
    site_dir = os.path.join(here, "_site")
    assert os.path.exists(site_dir)


if __name__ == "__main__":
    simple_test()
    print("Test passed. Compiled blog site directory exists.")
