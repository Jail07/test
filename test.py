def chains(h, k):
    count = 1
    for i in range(len(h) - 1):
        if abs(h[i] - h[i + 1]) > k:
            count += 1
    return count

def find_k(n, m, h):
    low = 0
    high = 1000000
    out = -1

    while low <= high:
        mid = (low + high) // 2
        с = chains(h, mid)

        if с == m:
            result = mid
            high = mid - 1
        elif с < m:
            high = mid - 1
        else:
            low = mid + 1

    return out

n, m = input().split()
n, m = int(n), int(m)
h = [int(x) for x in input().split()]

out = find_k(n, m, h)

print(out)
