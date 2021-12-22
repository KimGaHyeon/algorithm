def hanoi (num, start, end, other):
    if num == 0:
      return;

    # 가장 아래 원반을 제외한 원반들을 도우미로 옮
    hanoi(num - 1, start, other, end)

    # 가장 아래 원반을 목적지로 옮김
    print(start, "번에서 ", end, "로 옮긴다.")

    # 도우미로 옮겼던 원반들을 목적지로 옮김
    hanoi(num - 1, other, end, start);

hanoi(3, 0, 2, 1);