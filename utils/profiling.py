import math
import time
from functools import wraps


def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        measurements = []
        result = None

        for i in range(5):
            t1 = time.time()
            result = fn(*args, **kwargs)
            t2 = time.time()
            measurements.append(t2 - t1)

        mean = sum(measurements) / len(measurements)
        variance = sum([(x - mean)**2 for x in measurements]) / len(measurements)
        std = math.sqrt(variance)

        print(f'@timefn: {fn.__name__} took {mean} seconds on average (std={std}).')

        return result

    return measure_time
