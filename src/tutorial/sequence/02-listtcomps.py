from memory_profiler import profile

@profile
def forloop():
    symbols = '!@#$%'
    codes = []
    for symbol in symbols:
        codes.append(ord(symbol))

    return codes

@profile
def listcomp():
    symbols = '!@#$%'
    codes = [ord(symbol) for symbol in symbols]
    return codes

if __name__ == '__main__':
    print(listcomp())