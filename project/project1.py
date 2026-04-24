import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

while True:
    print("\n1. Ввести список")
    print("2. Случайный список")
    print("0. Выход")
    choice = input("Выбор: ")

    if choice == "0":
        break
    elif choice == "1":
        numbers = list(map(int, input("Числа через пробел: ").split()))
    elif choice == "2":
        numbers = [random.randint(1, 99) for _ in range(8)]
        print("Список:", numbers)
    else:
        print("Неверный выбор!")
        continue

    print("\n1. Пузырьковая  2. Выбором  3. Вставками")
    alg = input("Алгоритм: ")

    result = numbers.copy()
    if alg == "1":
        result = bubble_sort(result)
    elif alg == "2":
        result = selection_sort(result)
    elif alg == "3":
        result = insertion_sort(result)
    else:
        print("Неверный алгоритм!")
        continue

    print("До:    ", numbers)
    print("После: ", result)