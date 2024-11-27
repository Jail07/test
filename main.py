n, m = input().split()
n = int(n)
m = int(m)
k = [i for i in input().split()]
l = [i for i in range(n)]
l = l[::-1]

f = [k.index(i)+1 for i in k]
count = len(l) - len(k)

for i in f:
    count += i*2
print(count)

# for i in l:
#     count+=1
#     if i in k:
#         count +=2








