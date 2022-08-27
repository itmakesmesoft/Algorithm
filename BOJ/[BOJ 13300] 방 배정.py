n, accept = map(int, input().split())
students = [[] for _ in range(2)]
for i in range(n):
    gender, grade = map(int, input().split()) # gender 0:여, 1:남
    students[gender].append(grade)
total = 0
for k in range(2):
    bucket = [0]*7
    for i in range(len(students[k])): # 카운트
        index = students[k][i]
        bucket[index] += 1

    for i in range(1,7):
        number = bucket[i]
        total += number//accept
        if number%accept>0:
            total += 1
print(total)