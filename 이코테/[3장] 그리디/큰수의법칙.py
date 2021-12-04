n,m,k = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
# 가장 큰수를 k번 더하고 두번째 큰수를 1번 더한다
nums.sort()
first = nums[-1]
second = nums[-2]

# while True:
#     for _ in range(k):
#         if m==0:
#             break
#         answer += first
#         m -= 1
#     if m == 0:
#         break
#     answer += second
#     m -= 1

count = int(m/(k+1)) * k
count += m%(k+1)

answer += count*first
answer += (m-count)*second
print(answer)