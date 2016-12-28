#!/usr/bin/env python
import os


HERE = os.path.dirname(os.path.realpath(__file__))
SITE_DIR = os.path.join(HERE, "_site")


def _item_exists(relpath):
    item = os.path.join(SITE_DIR, relpath)
    assert os.path.exists(item), "FAILED: {} does not exist".format(item)
    print("PASSED: {} exists".format(item))


def output_dir():
    assert os.path.exists(SITE_DIR), "FAILED: _site/ does not exist"
    print("PASSED: Compiled blog site directory exists.")


def main():
    output_dir()
    to_check = ["index.html", "assets", "feed.xml", "tags", "archives"]
    for item in to_check:
        _item_exists(item)


if __name__ == "__main__":
    main()
