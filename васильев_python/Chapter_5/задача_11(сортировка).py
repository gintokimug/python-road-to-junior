def insert_sort(A):
    """ сортировка списка A вставками"""
    N = len(A)
    for top in range(1, N):
        k = top
        if k > 0 and A[k - 1] > A[k]:
            A[k], A[k - 1] = A[k - 1], A[k]
            k -= 1
def choice_sort(A):
    """ сортировка списка A выбором"""
    N = len(A)
    for position in range(0, N - 1):
        for k in range(position + 1, N):
            if A[k] < A[position]:
                A[k], A[position] = A[position], A[k]
def buble_sort(A):
    """сортировка А методом пузырька"""
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N - bypass):
            if A[k] > A[k + 1]:
                A[k], A[k + 1] = A[k + 1], A[k]
def test_sort(sort_aloritm):
    print("testcase #1: ", end = "" )
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_aloritm(A)
    if A == A_sorted:
        