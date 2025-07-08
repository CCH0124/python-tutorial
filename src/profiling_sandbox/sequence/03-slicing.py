
def slice_example():
    l = [1, 2, 3, 4, 5]
    print(f'from start 0 to 1 {l[:2]}')
    print(f'from start 2 to last {l[2:]}')

def slice_example02():
    l = list(range(10))
    print(f'init l: {l}')
    l[2:5] = [20, 30]
    print(f'insert from 2 to 4 : {l}')
    del l[5:7]
    print(f'del element from 5 to 6: {l}')
    l[3::2] = [11, 22]
    print(f'insert element from 3. step is 2: {l}')

if __name__ == "__main__":
    slice_example02()