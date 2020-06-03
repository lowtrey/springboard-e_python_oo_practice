"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):

        self.start = start

        self.num = None

    def generate(self):

        if self.num:

            self.num += 1

        else:

            self.num = self.start

        return self.num

    def reset(self):

        self.num = None

    def __repr__(self):

        if self.num:

            next = self.num + 1

        else:

            next = self.start + 1

        return f"<SerialGenerator start={self.start} next={next}>"
