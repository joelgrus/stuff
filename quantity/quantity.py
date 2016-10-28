# from solution.quantity import Quantity

class Quantity(object):
    pass


q = Quantity

def test_multiply():
    length = q('meters', 3)
    width = q('meters', 4)
    print '{} * {} = {}'.format(length, width, length * width)
    # 12 * meters^2


def test_divide():
    users = q('users', 10**4)
    req_per_user_day = q('requests', 5) / (q('users', 1) * q('day', 1))
    print '{} * {} = {}'.format(users, req_per_user_day, users * req_per_user_day)
    # 50000 * requests * day^-1


def test_power():
    length = q('millimeters', 5)
    print '{}^3 = {}'.format(length, length**3)
    # 125 * millimeters^3


def test_addition():
    print q('pencils', 2) + q('pencils', 3)
    try:
        print q('pencils', 2) + q('pens', 3)
    except Exception as e:
        print e


test_multiply()
test_divide()
test_power()
test_addition()
