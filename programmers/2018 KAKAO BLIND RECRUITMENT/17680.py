# https://programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities)*5
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        if city not in cache:
            if len(cache) == cacheSize:
                cache.pop()
            answer += 5
        else:
            cache.pop(cache.index(city))
            answer += 1
        cache.insert(0,city)
    return answer