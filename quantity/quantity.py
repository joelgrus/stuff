# from solution.quantity import Quantity

class Quantity(object):
    pass


q = Quantity

def test_multiply():
    length = q('meters', 3)
    width = q('meters', 4)
    print '\nmultiplication:\n{} * {}\n=\n{}'.format(length, width, length * width)
    # (something similar to) 12 * meters^2


def test_power():
    time = q('seconds', 1.3 * 10**-12)
    print '\nexponentiation:\n({})^-1\n=\n{}'.format(time, time**-1)
    # 7.69e+11 * seconds^-1


def test_divide():
    requests_per_day = q('requests', 10**6) / q('day')
    users_per_day = q('users', 3 * 10**4) / q('day')
    requests_per_user = requests_per_day / users_per_day
    print '\ndivision:\n{} / {}\n=\n{}'.format(requests_per_day, users_per_day, requests_per_user)
    # 33.33 requests * user^-1


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
    print '\nusability:\nneed {}\n({})\nfor {}\n(utilization: {})\n'.format(
                cores_needed,
                instances_deployed,
                scrapes_per_site * sites_per_day,
                utilization)


# TODO what else could we define?


test_multiply()
# test_power()
# test_divide()
# test_usability()
