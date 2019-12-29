import re

"""
Input : decimal
Output : maximum binary gap
# binary gap : 10001 -> number of 0 between 1

# N = len(str or sequence type)
# for i in range(N):
    str[i]
-> 이렇게 하면 됨
"""
def solution(N):
    decimal_to_binary = bin(N)
    binary_without_0b = decimal_to_binary[2:]
    position_1 = [m.start() for m in re.finditer('1',binary_without_0b)]
    max_num = 0
    num = position_1[0]
    for i in position_1:
        if num == i:
            continue

        if int(i) - int(num) > max_num:
            max_num = int(i) - int(num)

        num = i


    if max_num > 0 :    # index의 시작 값이 0이기 때문에
        max_num = max_num -1    # 1을 빼준다.
    return max_num
