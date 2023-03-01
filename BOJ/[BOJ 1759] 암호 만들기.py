L, C = map(int, input().split())
lst = list(input().split())
lst.sort()

def is_valid(str):
  con = vow = 0
  for i in range(L):
    if str[i] in ('a', 'e', 'i', 'o', 'u'): # 모음인 경우
      vow+=1
    else: # 자음인 경우
      con+=1
  # 자모음 갯수에 따라 True/False 반환
  if vow>=1 and con>=2: return True
  else: return False


# 2. DFS
def dfs(prev_idx, str, depth):
  if depth==L-1:  # 깊이가 L-1이면 자모음 갯수 검증
    if is_valid(str):
      print(str)  # 반환값이 True인 경우 print
    return
  # for문은 이전에 선택한 숫자보다 큰 숫자부터 C-1까지 순회
  for i in range(prev_idx+1, C):
    new_str = str+lst[i]
    dfs(i, new_str, depth+1)

# 1. 0번 인덱스부터 C-L+1번 인덱스까지 순회
for i in range(0, C-L+1):
  dfs(i, lst[i], 0)