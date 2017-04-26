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
    cycle_time = q('seconds', 4.2 * 10**-10)
    hz_conversion = q('seconds') * q('hertz')
    frequency = cycle_time**-1 * hz_conversion
    print '\nexponentiation:\n({})^-1\n=\n{}'.format(cycle_time, frequency)
    # 2.38e+09 * hertz


def test_divide():
    requests_per_day = q('requests', 10**6) / q('day')
    users_per_day = q('users', 3 * 10**4) / q('day')
    requests_per_user = requests_per_day / users_per_day
    print '\ndivision:\n{} / {}\n=\n{}'.format(requests_per_day, users_per_day, requests_per_user)
    # 33.33 requests * user^-1


def test_usability():
    scrapes_per_site = 10 * q('scrape') / q('site')
    sites_per_day = 5000 * q('site') / q('day')
    # assume we're CPU bound
    core_seconds_per_scrape = 15 * q('core') * q('second') / q('scrape')
    core_time_per_day = scrapes_per_site * sites_per_day * core_seconds_per_scrape
    seconds_per_day = 86000 * q('second') / q('day')
    cores_needed = core_time_per_day / seconds_per_day

    cores_per_instance = 4 * q('core') / q('c3.xlarge')
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
