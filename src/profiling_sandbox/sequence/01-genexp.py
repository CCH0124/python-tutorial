from memory_profiler import profile
import sys

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

@profile
def genexpexample():
    """
    return <generator>
    """
    gen_exp = (f'{c} {s}' for c in colors for s in sizes)
    print("生成器表達式佔用記憶體：", sys.getsizeof(gen_exp), "bytes")
    return gen_exp


@profile
def listcompexample():
    list_comp = [(c, s) for c in colors for s in sizes]
    print("列表推導式佔用記憶體：", sys.getsizeof(list_comp), "bytes")
    return list_comp


@profile
def listcompexample2():
    list_comp = [i**2 for i in range(1_000_000)]
    print("列表推導式佔用記憶體：", sys.getsizeof(list_comp), "bytes")

@profile
def genexpexample2():
    gen_exp = (i**2 for i in range(1_000_000))
    print("生成器表達式佔用記憶體：", sys.getsizeof(gen_exp), "bytes")

if __name__ == '__main__':
    print(listcompexample2())
    print(genexpexample2())