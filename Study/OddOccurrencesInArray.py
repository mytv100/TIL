"""
Input : Array that contains odd numbers of element
Output : unpaired element

# A[0] = 1, A[1] = 1
# A[2] = 2, A[3] = 2
# A[4] = 5 -> unpaired
"""
def solution(A):
    dict_element = {}

    for i in A:
        if i not in dict_element:
            dict_element[i] = 1
        else:
            dict_element[i] = dict_element[i] + 1

    for key, value in dict_element.items():
        if value % 2 == 0:
            continue
        else:
            unpaired_value = key

    return unpaired_value
