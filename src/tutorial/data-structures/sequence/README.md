1. 容器 Sequence
可以保存不同型態的項目，包括嵌套容器: list、tuple 與 collections.deque
2. 平面 Sequence
保存一種簡單型態的項目。例如: str、bytes 與 array.array

可以從可變性來分類
1. 可變的 Sequence
- list、bytearray、array.array 和 collections.deque
2. 不可變的 Sequence
- tuple、str 與 bytes

串列生成式 *listtcomps*

產生器表達式 *genexps*
- 節省記憶體

### tuple vs list

- 對於 `tuple(t)` 僅回傳一個 `t` 的參考，無須進行複製。`list` 而言，`list(l)` 建構式一定會建立 `l` 的新副本。
- tuple 實例配置會是剛好的記憶體空間。`list` python 會而外配置備用空間。

將 tuple 視為不可變 list 有兩大好處
1. 明確
- 一旦看到 tuple，即長度絕不可變
2. 效能
- tuple 記憶體使用比 list 還少

```python
@profile
def listcompexample2():
    list_comp = [i**2 for i in range(1_000_000)]
    print("列表推導式佔用記憶體：", sys.getsizeof(list_comp), "bytes")

@profile
def genexpexample2():
    gen_exp = (i**2 for i in range(1_000_000))
    print("生成器表達式佔用記憶體：", sys.getsizeof(gen_exp), "bytes")

```

```bash
python -m memory_profiler src/profiling_sandbox/sequence/genexp.py 
```

### slice
slice 與 range 不含最後項目，其從零算起。

```bash
$ poetry run python src/profiling_sandbox/sequence/slicing.py
from start 0 to 1 [1, 2]
from start 2 to last [3, 4, 5]
```

`s[a:b:c]` 可以透過 `c` 指定跨距。為了計算 `seq[start:stop:step]`，Python 會呼叫 `seq.__getitem__(slice(start, stop, step))`

```bash
$ poetry run python src/profiling_sandbox/sequence/slicing.py
init l: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
insert from 2 to 4 : [0, 1, 20, 30, 5, 6, 7, 8, 9]
del element from 5 to 6: [0, 1, 20, 30, 5, 8, 9]
insert element from 3. step is 2: [0, 1, 20, 11, 5, 22, 9]
```

### Sequence 的 + 與 *

串接多個同一 `sequence` 的多副本，將其乘以一個整數，這會產生一個新 `sequence`，`+` 也是。

```python
>>> l = [1, 2, 3]
>>> l * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> 5 * 'abc'
'abcabcabcabcabc'
>>>
```

### Sequence 擴增賦值

擴增賦值可以是
- `+=`
  - `__iadd__`
- `*-`
  - `__imul__`

```python
>>> l = [1,2]
>>> l *= 2
>>> l
[1, 2, 1, 2]
>>> t = ('a', 'b', 'c')
>>> id(t)
140515865236480
>>> t *= 2
>>> t
('a', 'b', 'c', 'a', 'b', 'c')
>>> id(t)
140515865218208
>>> 
```

 
> [!TIP]
>list 是在同一物件；但 tuple 會建立新物件
>**不要把可變的項目放入 `tuple`**

### list.sort vs sorted
1. list.sort
- 不會製作副本
- 透過回傳 None 告知改變了 receiver，且沒有建立新的 list

2. sorted
- 建立新的 list 且回傳

上述的排序都接收兩種可選關鍵字

1. reverse
2. key
- 產生排序鍵