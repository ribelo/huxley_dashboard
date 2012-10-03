import json
import re
import os


def parse_json(filename):
    """docstring for parse_json"""
    # Regular expression for comments
    comment_re = re.compile('(^)?[^\S\n]*(\#)(?:.*)($)?')
    with open(filename) as f:
        content = ''.join(f.readlines())

        # Looking for comments
        match = comment_re.search(content)
        while match:
            # single line comment
            content = content[:match.start()] + content[match.end():]
            match = comment_re.search(content)

        # Return json file
        return json.loads(content)


def settings(filename, *args):
    """ Returning a value from json file """
    # filepath = os.path.join('./module/', filename)
    setting = parse_json(filename)
    for key in args:
        setting = setting[key]
    return setting
