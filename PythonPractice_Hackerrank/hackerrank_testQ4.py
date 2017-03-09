import math

def  subarray_median(arr, k):
    sublist = [i for i in arr if i <=k]
    sublist = sorted(sublist)
    print(sublist)
    print("Floor is {0}".format(math.floor(len(sublist)/2)))
    median = arr[math.floor(len(sublist)/2)] if len(sublist)% 2 != 0 else (arr[math.floor(len(sublist)/2)-1]+arr[math.floor(len(sublist)/2)])/2
    return median


_arr_cnt = 0
_arr_cnt = int(input())
_arr_i=0
_arr = []
while _arr_i < _arr_cnt:
    _arr_item = int(input());
    _arr.append(_arr_item)
    _arr_i+=1



_k = int(input());

res = subarray_median(_arr, _k)
print(res)
