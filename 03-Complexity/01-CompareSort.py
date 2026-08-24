# sorting algorithms comparison
# insertion sort, selection sort, bubble sort, merge sort, quick sort



import random
import time


# --------------------------------
# Selection Sort
# --------------------------------
"""
Selection Sort

핵심 아이디어:
- 가장 작은 값을 찾아 앞쪽부터 배치한다.

시간복잡도:
- O(n^2)
"""

def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# --------------------------------
# Quick Sort
# --------------------------------
"""
Quick Sort

핵심 아이디어:
- 하나의 값을 Pivot으로 선택한다.
- Pivot보다 작은 값과 큰 값으로 나눈다.
- 나누어진 부분을 재귀적으로 정렬한다.

알고리즘 설계 방법:
- Divide and Conquer (분할 정복)

시간복잡도:
- 평균: O(n log n)
- 최악: O(n^2)
"""
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)

        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


# --------------------------------
# 실행 시간 비교
# --------------------------------
N = 10000

data = [random.randint(1, 100000) for _ in range(N)]

# 동일한 데이터를 사용하기 위해 복사
data1 = data.copy()
data2 = data.copy()


# Selection Sort
start = time.perf_counter()

selection_sort(data1)

end = time.perf_counter()

print("Selection Sort :", end - start, "sec")


# Quick Sort
start = time.perf_counter()

quick_sort(data2, 0, len(data2) - 1)

end = time.perf_counter()

print("Quick Sort     :", end - start, "sec")