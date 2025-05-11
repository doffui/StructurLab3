from collections import deque
import time
import tracemalloc

def joseph_array_a(n, m):
    people = list(range(1, n + 1))
    idx = 0
    while len(people) > 1:
        idx = (idx + m - 1) % len(people)
        people.pop(idx)
    return people[0]


def joseph_linked_list_a(n, m):
    head = curr = Node(1)
    for i in range(2, n + 1):
        curr.next = Node(i)
        curr = curr.next
    curr.next = head

    while curr.next != curr:
        for _ in range(m - 1):
            curr = curr.next
        curr.next = curr.next.next
    return curr.value


def joseph_deque_a(n, m):
    dq = deque(range(1, n + 1))
    while len(dq) > 1:
        dq.rotate(-(m - 1))
        dq.popleft()
    return dq[0]


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

def joseph_standard(n, m):
    res = 0
    for i in range(2, n + 1):
        res = (res + m) % i
    return res + 1

def find_start_optimized(n, m, l):
    j_standard = joseph_standard(n, m)
    shift = (l - j_standard + n) % n
    start = shift + 1
    return start if start != 0 else n

def measure(func, *args):
    tracemalloc.start()
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    time_taken = end_time - start_time
    memory_used_kb = peak / 1024  # Переводим в килобайты
    return result, time_taken, memory_used_kb

def main():
    print("Работу выполнила: Захарова Анастасия Григорьевна 09.03.01ПОВа-o24")
    print("=== Задача а) ===")
    n = int(input("Введите количество людей N: "))
    m = int(input("Введите шаг M: "))

    result_array_a, time_a1, mem_a1 = measure(joseph_array_a, n, m)
    result_linked_a, time_a2, mem_a2 = measure(joseph_linked_list_a, n, m)
    result_deque_a, time_a3, mem_a3 = measure(joseph_deque_a, n, m)

    print(f"\nОстался человек под номером: {result_array_a} (через массив)")
    print(f"Остался человек под номером: {result_linked_a} (через связанный список)")
    print(f"Остался человек под номером: {result_deque_a} (через deque)")


    print("\n=== Задача б) ===")
    l = int(input("Введите номер оставшегося человека L: "))

    result_optimized, time_optimized, mem_optimized = measure(find_start_optimized, n, m, l)

    print(f"\nЧтобы остался {l}, нужно начать с: {result_optimized}")
    print(f"Время выполнения (оптимизированная): {time_optimized:.6f} с")
    print(f"Память (оптимизированная): {mem_optimized:.3f} КБ")


    print("\n=== Производительность задачи а) ===")
    print("Затраченное время и память:")
    print(f"joseph_array_a     : {time_a1:.6f} с, {mem_a1:.3f} КБ")
    print(f"joseph_linked_list_a: {time_a2:.6f} с, {mem_a2:.3f} КБ")
    print(f"joseph_deque_a     : {time_a3:.6f} с, {mem_a3:.3f} КБ")


if __name__ == "__main__":
    main()
