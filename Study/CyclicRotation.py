"""
Input : Array, rotatation number
Output : rotated Array

# ([1,2,3,4],2)
# >>> [3,4,1,2]
"""
def solution(A, K):

    num = len(A)
    if num == 0:
        return A

    for i in range(K):
        A.insert(0,A[num-1])
        del A[num]
    return A
