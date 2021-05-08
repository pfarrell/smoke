import random
import sys
import csv
from string import punctuation, digits, ascii_uppercase, ascii_lowercase, ascii_letters


def _rnd(stop, start=0, step=1):
    return random.randrange(start, stop, step)


def _punc():
    v = _rnd(32)
    return punctuation[v]


def _num():
    v = _rnd(10)
    return digits[v]


def _ucase():
    v = _rnd(26)
    return ascii_uppercase[v]


def _lcase():
    v = _rnd(26)
    return ascii_lowercase[v]


def _alpha():
    v = _rnd(52)
    return ascii_letters[v]


def swap(char):
    if char in punctuation:
        return _punc()
    elif char in digits:
        return _num()
    elif char in ascii_uppercase:
        return _ucase()
    elif char in ascii_lowercase:
        return _lcase()


if __name__ == '__main__':
    # random.seed(1)
    csv_reader = csv.reader(sys.stdin)
    csv_writer = csv.writer(sys.stdout)
    for row in csv_reader:
        swapped = []
        for elem in row:
            s = ""
            for char in elem:
                s = s + swap(char)
            swapped.append(s)
        csv_writer.writerow(swapped)
