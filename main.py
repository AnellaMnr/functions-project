import functools
import time


def clock(func):
    calls = 0
    global_time = 0
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        nonlocal calls, global_time

        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        delta_t = time.perf_counter() - t0
        global_time += delta_t

        calls += 1

        arglist = []

        if args:
            arglist.extend(['{0}'.format(repr(arg)) for arg in args])

        if kwargs:
            kwlist = ['{0}={1}'.format(k, w) for k, w in kwargs.items()]
            arglist.extend(kwlist)

        argstr = ' ,'.join(arglist)

        print(
            'call# : {:2d} - {:0.8f} - {:0.8f} - {}({}) = {}'.format(
                calls, delta_t, global_time, func.__name__, argstr, result
            )
        )

        return result

    return clocked


@functools.lru_cache()
@clock
def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


n = 10
print(fib.__name__, "(", n, ") = ", fib(n), sep="")