from copy import deepcopy


# https://atcoder.jp/contests/abc429/tasks/abc429_b
n, m = map(int, input().split())
array_a = list(map(int, input().split()))


def check(base_arr) -> bool:
    for i, elm in enumerate(base_arr):
        tmp_arr = deepcopy(base_arr)
        tmp_arr.pop(i)
        if sum(tmp_arr) == m:
            return True
    return False


print("Yes") if check(base_arr=array_a) else print("No")
