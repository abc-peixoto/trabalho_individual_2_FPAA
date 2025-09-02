from typing import Iterable, Tuple, List


def maxmin_select(arr: Iterable[int]) -> Tuple[int, int]:
    arr = list(arr)
    n = len(arr)
    if n == 0:
        raise ValueError("Sequência vazia.")
    if n == 1:
        return arr[0], arr[0]
    if n == 2:
        a, b = arr[0], arr[1]
        return (a, b) if a <= b else (b, a)
    mid = n // 2
    mn1, mx1 = maxmin_select(arr[:mid])
    mn2, mx2 = maxmin_select(arr[mid:])
    mn = mn1 if mn1 <= mn2 else mn2
    mx = mx1 if mx1 >= mx2 else mx2
    return mn, mx


def main():
    try:
        raw = input("Digite os números separados por espaço: ").strip()
        nums: List[int] = list(map(int, raw.split()))
    except ValueError:
        print("Entrada inválida.")
        return

    mn, mx = maxmin_select(nums)
    print("Menor:", mn)
    print("Maior:", mx)


if __name__ == "__main__":
    main()
