
class Quantity(object):
    pass


from unit import Quantity

def test():
    q = Quantity
    users = q('users', 10**4)
    req_per_user_day = q('requests', 5) / (q('users') * q('day'))

    print users * req_per_user_day

    # more


test()
