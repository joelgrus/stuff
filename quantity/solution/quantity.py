# cheating isn't cool

from __future__ import division


class Quantity(object):

    # tempting to set self.units to a string at first
    def __init__(self, units, magnitude=1):
        self.magnitude = float(magnitude)
        if isinstance(units, basestring):
            self.units = {units.rstrip('s'): 1}
        else:
            self.units = {u.rstrip('s'): v for u, v in units.items() if v != 0}

    # generally have to tell people about __mul__ and its friends
    # though they could also look at set(dir(float)) - set(dir(object))
    def __mul__(a, b):
        if isinstance(b, Quantity):
            magnitude = a.magnitude * b.magnitude
            units = {u: a.units.get(u, 0) + b.units.get(u, 0)
                         for u in a.units.keys() + b.units.keys()}
            return Quantity(units, magnitude)
        else:
            return Quantity(a.units, a.magnitude * b)

    # commutative
    __rmul__ = __mul__

    # easier to define division as ^-1
    def __pow__(a, b):
        if isinstance(b, int):
            magnitude = a.magnitude ** b
            units = {d: a.units[d] * b for d in a.units}
            return Quantity(units, magnitude)
        else:
            raise TypeError("no")

    def __div__(a, b):
        return a * b**-1

    # not sure if a concise general definition with / or __div__ is possible
    def __rdiv__(b, a):
        return a * b**-1

    def __add__(a, b):
        if a.units != b.units:
            raise ValueError("only add things with the same units :(")
        return Quantity(a.units, a.magnitude + b.magnitude)

    __radd__ = __add__

    def __sub__(a, b):
        return a + -1*b

    def __rsub__(b, a):
        return a + -1*b

    def __eq__(a, b):
        return (a.magnitude == b.magnitude) and (a.units == b.units)

    def __str__(self):
        units = [dim + ('s' if power > 0 else '') + (('^' + str(power)) if power != 1 else '')
                 for dim, power in sorted(self.units.items(), key=lambda x:x[1], reverse=True)]
        magnitude_format = ('{:.0f}' if self.magnitude.is_integer()
                            else '{:.2f}' if (.01 < self.magnitude < 10000)
                            else '{:.4e}')
        return magnitude_format.format(self.magnitude) + ' ' + ' * '.join(units)
