# -*- coding: utf-8 -*-
"""
Utility functions
"""


import os.path
from requests import Session


_ROOT = os.path.abspath(os.path.dirname(__file__))

SESSION_PATH = os.path.join(_ROOT, 'session.txt')

if os.path.isfile(SESSION_PATH):
    with open(os.path.join(_ROOT, SESSION_PATH), 'r') as file:
        COOKIES = dict(session=file.read())
else:
    COOKIES = None


def get_input(year, day):
    path = os.path.join(_ROOT, 'input', f'year{year}', f'day{day}.txt')
    
    if os.path.isfile(path):
        with open(path, 'r') as file:
            return file.read()
    
    if COOKIES is None:
        raise FileNotFoundError(('Add session id to aoc/session.txt '
                                 f'or paste the input here: {path}'))
    
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    text = Session().get(url, cookies=COOKIES).text
    with open(path, 'w') as file:
        file.write(text)
    
    return text
    