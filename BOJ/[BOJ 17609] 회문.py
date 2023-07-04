# 왼쪽 끝, 오른쪽 끝에서 한칸씩 안으로 이동하면서 비교
# 만약 서로 다른 경우, 왼쪽-1과 비교 => 같지 않으면
#                   오른쪽-1과 비교=> 같지 않으면 팰린드롬x
#                                   같으면 유사 팰린드롬 가능성있음
#                   이후 계속 같으면 유사 팰린드롬
#                   하나라도 틀리면 팰린드롬 x

def is_palindrome(word, status):
    n = len(word)
    left, right = 0, n-1
    while left<=right:
        if word[left]==word[right]:
            pass
        else:
            if status==1: return 2
            elif word[left+1]==word[right] or word[left]==word[right-1]:
                a = is_palindrome(word[left+1:right+1], 1)
                b = is_palindrome(word[left:right], 1)
                return min(a, b)
            else: return 2
        left+=1
        right-=1
    return status


T=int(input())
for _ in range(T):
    word = input()
    print(is_palindrome(word, 0))

    # cabaca => 1이어야 함