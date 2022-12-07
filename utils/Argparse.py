import argparse

class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parserSet()
        self.args = self.parser.parse_args()

    def parserSet(self):
        self.parser.add_argument('--user', type=int, default=1)