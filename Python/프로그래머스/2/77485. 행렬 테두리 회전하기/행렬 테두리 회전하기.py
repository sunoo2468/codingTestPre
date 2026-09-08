def solution(rows, columns, queries):
    answer = []
    
    # step1. 행렬 만들기
    matrix = []
    number = 1
    
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(number)
            number += 1
        matrix.append(row)
        
    # step2. 회전된 쿼리 행렬에 반영하기
    for k in range(len(queries)):
        x1 = queries[k][0] - 1
        y1 = queries[k][1] - 1
        x2 = queries[k][2] - 1
        y2 = queries[k][3] - 1

        change = matrix[x1][y1]
        smallest = matrix[x1][y1]

        # 위쪽
        for y in range(y1, y2):
            temp = matrix[x1][y + 1]
            matrix[x1][y + 1] = change
            change = temp
            smallest = min(change, smallest)
            
        # 오른쪽
        for x in range(x1, x2):
            temp = matrix[x + 1][y2]
            matrix[x+1][y2] = change
            change = temp
            smallest = min(change, smallest)
            
        # 아래쪽
        for y in range(y2, y1, -1):
            temp = matrix[x2][y - 1]
            matrix[x2][y - 1] = change
            change = temp
            smallest = min(change, smallest)
            
        # 왼쪽
        for x in range(x2, x1, -1):
            temp = matrix[x - 1][y1]
            matrix[x-1][y1] = change
            change = temp
            smallest = min(change, smallest)
            
        answer.append(smallest)
        
    return answer
        