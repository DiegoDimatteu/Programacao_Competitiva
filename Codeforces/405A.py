a = int(input())
b = [int(i) for i in input().split()]
b.sort()
print(*b, sep = ' ')