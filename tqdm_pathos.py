import os
from itertools import repeat
from tqdm import tqdm
import pathos.pools


CPUs = os.cpu_count()


def get_chunksize(n_tasks, n_cpus):
    
    chunksize, remainder = divmod(n_tasks, n_cpus*4)
    if remainder:
        chunksize += 1

    return chunksize
    
    
def func_map(func_iterable_args_kwargs):

    func, iterable, args, kwargs = func_iterable_args_kwargs
    
    return func(*[iterable] + args, **kwargs)
    

def func_starmap(func_iterables_args_kwargs):

    func, iterables, args, kwargs = func_iterables_args_kwargs
    
    return func(*list(iterables) + args, **kwargs)
    
    
def map_or_starmap(which, func, iterable, args, kwargs):

    n_cpus = kwargs.pop('n_cpus', CPUs)
    pool = kwargs.pop('pool', None)

    iterable = list(iterable)
    n_tasks = len(iterable)
    
    func_iterable_args_kwargs = zip(
        repeat(func),
        iterable,
        repeat(list(args)),
        repeat(kwargs),
        )

    if which == 'map':
        _func = func_map
    elif which == 'starmap':
        _func = func_starmap
        
    if pool is not None:
        chunksize = get_chunksize(n_tasks, len(pool._pool))
        return list(tqdm(pool.imap(_func, func_iterable_args_kwargs, chunksize), total=n_tasks))
        
    with pathos.pools._ProcessPool(n_cpus) as pool:
        chunksize = get_chunksize(n_tasks, n_cpus)
        return list(tqdm(pool.imap(_func, func_iterable_args_kwargs, chunksize), total=n_tasks))


def map(func, iterable, *args, n_cpus=CPUs, pool=None, **kwargs):

    return map_or_starmap('map', func, iterable, args, {**{'n_cpus': n_cpus, 'pool': pool}, **kwargs})
    

def starmap(func, iterables, *args, n_cpus=CPUs, pool=None, **kwargs):

    return map_or_starmap('starmap', func, iterables, args, {**{'n_cpus': n_cpus, 'pool': pool}, **kwargs})
        

