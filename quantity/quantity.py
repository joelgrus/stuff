# from solution.quantity import Quantity

class Quantity(object):
    pass


q = Quantity

def test_multiply():
    length = q('meters', 3)
    width = q('meters', 4)
    print '{} * {} = {}'.format(length, width, length * width)
    # (something similar to) 12 * meters^2


def test_power():
    length = q('millimeters', 5)
    print '{}^3 = {}'.format(length, length**3)
    # 125 * millimeters^3


def test_divide():
    users = q('users', 10**4)
    req_per_user_day = q('requests', 5) / (q('users', 1) * q('day', 1))
    print '{} * {} = {}'.format(users, req_per_user_day, users * req_per_user_day)
    # 50000 * requests * day^-1


def test_usability():
    scrapes_per_site = 10 * q('scrapes') / q('site')
    sites_per_day = 5000 * q('sites') / q('day')
    # assume we're CPU bound
    core_seconds_per_scrape = 15 * q('core') * q('seconds') / q('scrape')
    core_time_per_day = scrapes_per_site * sites_per_day * core_seconds_per_scrape
    seconds_per_day = 86000 * q('seconds') / q('day')
    cores_needed = core_time_per_day / seconds_per_day

    cores_per_instance = 4 * q('cores') / q('c3.xlarge')
    instances_needed = cores_needed / cores_per_instance
    import math
    instances_deployed = math.ceil(instances_needed.magnitude) * q(instances_needed.units)
    utilization = instances_needed / instances_deployed
    print 'need {} ({}) for {} (utilization: {})'.format(
                cores_needed,
                instances_deployed,
                scrapes_per_site * sites_per_day,
                utilization)


# TODO what else could we define?


test_multiply()
# test_power()
# test_divide()
# test_usability()
