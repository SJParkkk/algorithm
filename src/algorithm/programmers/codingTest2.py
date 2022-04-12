def solution(grid):
    answer = -1
    columns = len(grid[0])
    nums = list(''.join(grid))
    table = [nums[i: i + columns] for i in range(0, len(nums), columns)]
    target_index =[(i, j) for i in range(columns) for j in range(len(table)) if table[i][j] == '?']
    number_of_cases = list()
    for i, j in target_index:
        print('i, j', i, j, columns, len(table))
        # y = j 고정
        xs, ys = [i-1, i+1], [j, j]
        nums = [table[x][y] for x, y in zip(xs, ys) if 0 <= x < columns]
        # x = i 고정
        xs, ys = [i, i], [j-1, j+1]
        col_num = [table[x][y] for x, y in zip(xs, ys) if 0 <= y < len(table)]
        nums.extend(col_num)
        k = set()
        for num in nums:
            k.add(num)
        if k:
            number_of_cases.append(k)
    if len(number_of_cases) == 1 and len(number_of_cases[0]) ==1:
        return 3
        #     if
        #
        #
        # for element in k:
        #     if element != '?':
        #         table[i][j] = element
        # print(table)

    return answer