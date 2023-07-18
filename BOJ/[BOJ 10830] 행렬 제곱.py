def Print(matrix):
    for i in range(N):
        print(*matrix[i])


def multiply(A, B):
    if A == 1:
        for i in range(N):
            for j in range(N):
                B[i][j] %= 1000
        return B

    matrix = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            for k in range(N):
                matrix[r][c] += (A[r][k] * B[k][c])
            matrix[r][c] = matrix[r][c] % 1000
    return matrix


N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]


answer = 1
while B > 0:
    if B%2 == 1:
        B-=1
        answer = multiply(answer, matrix)
    elif B%2==0:
        B//=2
        matrix = multiply(matrix, matrix)

Print(answer)