def solution(rows, columns, queries):
    answer = []
    nums = [i for i in range(1, rows*columns + 1)]
    # 이차원 배열 생성
    table = [nums[i: i+columns] for i in range(0, len(nums), columns)]
    for a,b,c,d in queries:
        start_y, start_x, end_y, end_x = a-1, b-1, c-1, d-1
        temp = table[start_y][start_x]
        small = temp

        # left : y + 1 이동
        for i in range(start_y+1, end_y+1):
            table[i-1][start_x] = table[i][start_x]
            small = min(small, table[i][start_x])

        # bottom : x - 1 이동
        for i in range(start_x + 1, end_x+1):
            table[end_y][i-1] = table[end_y][i]
            small = min(small, table[end_y][i])

        # right : y -1 이동
        for i in range(end_y-1, start_y-1, -1):
            table[i+1][end_x] = table[i][end_x]
            small = min(small, table[i][end_x])

        # top : x + 1 이동
        for i in range(end_x - 1, start_x, -1):
            table[start_y][i+1] = table[start_y][i]
            small = min(small, table[start_y][i])
        table[start_y][start_x+1] = temp
        # 최소값
        answer.append(small)
    return answer
