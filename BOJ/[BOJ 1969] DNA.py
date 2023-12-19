import sys
input = sys.stdin.readline

def get_max_count_with_index(cnt):
  max_count, max_index = 0, 0
  for index, num in enumerate(cnt):
    if num > max_count:
      max_count, max_index = num, index
  return (max_count, max_index)


N, M = map(int, input().split())
lst = [list(input().rstrip()) for _ in range(N)]
total_dist = 0
dnas = ["A", "C", "G", "T"]
res_dna = ""
for i in range(M):
  count = [0]*4
  for j in range(N):
    for k in range(4):
      if lst[j][i]==dnas[k]:
        count[k]+=1
        break
  max_count, max_index = get_max_count_with_index(count)
  total_dist += (N - max_count)
  res_dna += dnas[max_index]

print(res_dna, total_dist, sep="\n")