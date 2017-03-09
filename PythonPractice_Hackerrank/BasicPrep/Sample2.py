def  summation(numbers):
    total = numbers[0]
    totalVal = 0
    print(total)
    for count in range(0,total):
        totalVal += numbers[count+1]
    print(totalVal)

_numbers_cnt = 0
_numbers_cnt = int(input())
_numbers_i=0
_numbers = []
while _numbers_i < _numbers_cnt:
    _numbers_item = int(input());
    _numbers.append(_numbers_item)
    _numbers_i+=1


res = summation(_numbers)
