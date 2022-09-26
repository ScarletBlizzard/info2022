import sys
import argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a')
    parser.add_argument('-b')

    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()

