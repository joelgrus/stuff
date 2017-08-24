# from solution.quantity import Quantity

class Quantity(object):

    def __init__(self, units, magnitude=None):
        pass


q = Quantity


def test_arithmetic():
    total_users = q('users', 1e4)
    premium_users = q('users', 7e2)
    standard_users = total_users - premium_users
    recalculated_total = standard_users + premium_users
    are_equal = total_users == recalculated_total
    print '{total_users} == {recalculated_total} is {are_equal}'.format(**locals())


def test_multiply():
    visible_area = q('pixels', 750 * 160)
    visible_time = q('seconds', 4.7)
    total_viewability = visible_area * visible_time
    print '\nmultiplication:'
    print '{visible_area} * {visible_time} = {total_viewability}'.format(**locals())
    # (something similar to) 5.64e+05 pixels * seconds


def test_power():
    cycle_time = q('seconds', 4.2 * 10**-10)
    hz_conversion = q('seconds') * q('hertz')
    frequency = cycle_time**-1 * hz_conversion
    print '\nexponentiation:'
    print '({cycle_time})^-1 = {frequency}'.format(**locals())
    # 2.38e+09 * hertz


def test_divide():
    requests_per_day = q('requests', 10**6) / q('day')
    users_per_day = q('users', 3 * 10**4) / q('day')
    requests_per_user = requests_per_day / users_per_day
    print '\ndivision:'
    print '{requests_per_day} / {users_per_day} = {requests_per_user}'.format(**locals())
    # 33.33 requests * user^-1


def test_usability():
    scrapes_per_site = 10 * q('scrape') / q('site')
    sites_per_day = 5000 * q('site') / q('day')
    scrapes_per_day = scrapes_per_site * sites_per_day
    # assume we're CPU bound
    core_seconds_per_scrape = 15 * q('core') * q('second') / q('scrape')
    core_time_per_day = scrapes_per_day * core_seconds_per_scrape
    seconds_per_day = 86000 * q('second') / q('day')
    cores_needed = core_time_per_day / seconds_per_day

    cores_per_instance = 4 * q('core') / q('c3.xlarge')
    instances_needed = cores_needed / cores_per_instance
    import math
    instances_deployed = math.ceil(instances_needed.magnitude) * q(instances_needed.units)
    utilization = instances_needed / instances_deployed
    print '\nusability:'
    print ('need {cores_needed} (= {instances_deployed})'
           ' for {scrapes_per_day} (utilization: {utilization})').format(**locals())


test_arithmetic()
test_multiply()
test_power()
test_divide()
test_usability()
