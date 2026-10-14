def solution(stones, k):
    left = 1
    right = max(stones) + 1

    while left < right:
        mid = (left + right) // 2
        consecutive = 0

        for stone in stones:
            if stone < mid:
                consecutive += 1
            else:
                consecutive = 0

            if consecutive >= k:
                break

        if consecutive >= k:
            right = mid
        else:
            left = mid + 1

    return left - 1