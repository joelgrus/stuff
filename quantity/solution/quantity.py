from __future__ import division


class Quantity(object):

    # tempting to set self.dimension to a string at first
    def __init__(self, dimension, magnitude=None):
        self.magnitude = magnitude
        if isinstance(dimension, basestring):
            self.dimension = {dimension: 1}
        else:
            self.dimension = {u: v for u, v in dimension.items() if v != 0}


    # generally have to tell people about __mul__ and its friends
    # though they could also look at set(dir(float)) - set(dir(object))
    def __mul__(a, b):
        if isinstance(b, Quantity):
            magnitude = (a.magnitude or 1) * (b.magnitude or 1)
            dimension = {u: a.dimension.get(u, 0) + b.dimension.get(u, 0)
                         for u in a.dimension.keys() + b.dimension.keys()}
            return Quantity(dimension, magnitude)
        else:
            return Quantity(a.dimension, (a.magnitude or 1) * b)

    # commutative
    __rmul__ = __mul__


    # easier to define division as ^-1
    def __pow__(a, b):
        if isinstance(b, int):
            magnitude = a.magnitude ** b
            dimension = {d: a.dimension[d] * b for d in a.dimension}
            return Quantity(dimension, magnitude)
        else:
            raise TypeError("no")


    def __div__(a, b):
        return a * b**-1

    # not sure if a concise general definition with / or __div__ is possible
    def __rdiv__(b, a):
        return a * b**-1


    def __add__(a, b):
        if a.dimension != b.dimension:
            raise ValueError("only add things with the same dimensions :(")
        return Quantity(a.dimension, a.magnitude + b.magnitude)

    __radd__ = __add__


    def __sub__(a, b):
        return a + -1*b

    def __rsub__(b, a):
        return a + -1*b


    def __repr__(self):
        numerator_dimension = ' * '.join(u + ('^{}'.format(p) if p > 1 else '')
                                     for u, p in self.dimension.items() if p > 0)
        denominator_dimension = ' * '.join(u + ('^{}'.format(p) if p < -1 else '')
                                     for u, p in self.dimension.items() if p < 0)
        r = '{:.2e} {}'.format(self.magnitude, numerator_dimension)
        if denominator_dimension:
            length = max(map(len, (r, denominator_dimension)))
            r += '\n{}\n{}'.format('-'*length, denominator_dimension)
        return r
