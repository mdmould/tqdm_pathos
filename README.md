# tqdm_pathos
Progress bars for multiprocessing with pathos

Wrappers based on [parmap](https://github.com/zeehio/parmap) for multiprocessing with [pathos](https://pathos.readthedocs.io/en/latest/pathos.html#module-pathos.pools) and progress bar completion with [tqdm](https://tqdm.github.io/). Following parmap, multiprocessing is extended to functions of multiple iterables, arguments, and keyword arguments.

While parmap includes these extensions and a progress bar, it is built on the default [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) library. The multiprocessing/pools module in pathos includes enhanced serialization to allow multiprocessing of, e.g., lambda functions, class methods, etc.

## Installation

You can `pip install tqdm-pathos`.

## Usage

A pool with an automatically detected number of cores is set up by default. To choose the number of cores, use the `n_cpus` kwarg.
Alternatively, an existing pool can be used by passing it to the `pool` kwarg.
Extra `kwargs` can be passed to the `tqdm` progress bar using the `tqdm_kwargs` dictionary argument, e.g., `tqdm_kwargs = {'desc': 'pbar description'}`.

Function of a single iterable:
```python
f = lambda x: x**2
iterable = [1, 2, 3]

# Serial
y = [f(x) for x in iterable]

# Parallel
y = tqdm_pathos.map(f, iterable)
```

Function of a single iterable, with non-iterable args and kwargs:
```python
def f(x, a, b=0):
    return x**2 * a + b
iterable = [1, 2, 3]
a = 1
b = 0
    
# Serial
y = [f(x, a, b=b) for x in iterable]

# Parallel
y = tqdm_pathos.map(f, iterable, a, b=b)
```

Function of multiple iterables:
```python
f = lambda x, y: x * y
iterable1 = [1, 2, 3]
iterable2 = [4, 5, 6]

# Serial
z = [f(x, y) for x, y in zip(iterable1, iterable2)]

# Parallel
z = tqdm_pathos.starmap(f, zip(iterable1, iterable2))
```

Function of multiple iterables, with non-iterable args and kwargs:
```python
def f(x, y, a, b=0):
    return x * y * a + b
iterable1 = [1, 2, 3]
iterable2 = [4, 5, 6]
a = 1
b = 0

# Serial
z = [f(x, y, a, b=b) for x, y in zip(iterable1, iterable2)]

# Parallel
z = tqdm_pathos.starmap(f, zip(iterable1, iterable2), a, b=b)
```

