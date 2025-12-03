from timeit import timeit
import random

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key
    return lst

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи,
	# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def test_sorted(data):
    return sorted(list(data))

def test_sort(data):
    d = list(data)
    d.sort()
    return d

def test_insertion_sort(data):
    insertion_sort(list(data))

def test_merge_sort(data):
    merge_sort(list(data))

def generate_data(number):
    return [random.randint(0, 10_000) for _ in range(number)]


if __name__ == '__main__':
    sizes = [1000, 5000, 10000]
    for size in sizes:
        print(f"\n===Тест для {size} елементів ===")
        data = generate_data(size)
        print("sorted() (Timsort): ", timeit(lambda: test_sorted(data), number=10))
        print("list.sort() (Timsort): ", timeit(lambda: test_sort(data), number=10))
        print("Insertion sort: ", timeit(lambda: test_insertion_sort(data), number=10))
        print("Merge sort: ", timeit(lambda: test_merge_sort(data), number=10))
