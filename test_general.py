"""General tests for all MHB plugins."""
import os
import re
import sqlite3
import sys

PATH = '.'
PLUGINPATH = '../sopel_*/*'
sys.path.append(PATH)


def test_line_length():
    """Checks line length."""
    MAX_LENGTH = 265 + 1
    for top, dirs, files in os.walk(PLUGINPATH):
        for filen in files:
            if not filen.endswith('.py'):
                continue
            with open(os.path.join(PLUGINPATH, filen)) as python_source:
                src = python_source.readlines()
                for line_number, line in enumerate(src):
                    assert len(line.strip()) < MAX_LENGTH, 'length of line #{0} exceeds limit'.format(line_number)


def test_no_get_on_lists():
    """Checks for misuse of .get() on lists."""
    reg = r'get\([0-9]'
    for top, dirs, files in os.walk(PLUGINPATH):
        for filen in files:
            if not filen.endswith('.py'):
                continue
            with open(os.path.join(PLUGINPATH, filen)) as python_source:
                src = python_source.read()
                assert not re.search(reg, src)
