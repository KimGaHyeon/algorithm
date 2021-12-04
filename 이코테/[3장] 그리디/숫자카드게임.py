n,m = map(int, input().split())
result = 0
for _ in range(n):
    cards = list(map(int,input().split()))
    min_val = min(cards)
    result = max(min_val,result)

print(result)