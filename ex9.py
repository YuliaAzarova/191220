spisok = []
s = 0
for x in range(10):
    A = int(input())
    s += A
    spisok.append(A)
sredn_ar = s // 10
answer = 0
for elem in spisok:
    if elem > sredn_ar:
        answer += 1
    print(answer)