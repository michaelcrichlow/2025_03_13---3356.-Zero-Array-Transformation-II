# 3356. Zero Array Transformation II

# 1.) Testcases passed!
# 2.) WORKS! Time Limit Exceeded 622 / 627 testcases passed
def minZeroArray_01(nums: list[int], queries: list[list[int]]) -> int:
    if sum(nums) == 0:
        return 0
    
    count = 0
    
    for val in queries:
        idx = val[0]
        for _val in nums[val[0]:val[1] + 1]:
            nums[idx] = _val - val[2] if _val - val[2] >= 0 else 0
            idx += 1

        count += 1
        if sum(nums) == 0:
            return count

    return -1


# 1.) Testcases passed!
# 2.) Solution accepted!
def minZeroArray(nums: list[int], queries: list[list[int]]) -> int:
    N = len(nums)
    Q = len(queries)

    left = 0
    right = Q + 1

    # what is good? Define that here...
    def good(target):
        diff = [0] * (N + 1)

        for l, r, v in queries[:target]:
            diff[l] += v
            diff[r + 1] -= v
        
        current = 0
        for i in range(N):
            current += diff[i]

            if current < nums[i]:
                return False
        return True
        
    while left < right:
        mid = (left + right) // 2

        if good(mid):
            right = mid
        else:
            left = mid + 1

    if left > Q:
        return -1
    
    return left



def main() -> None:
    print(minZeroArray(nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]])) # 2
    print(minZeroArray(nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]])) # -1
    print(minZeroArray(nums = [0], queries = [[0,0,2],[0,0,4],[0,0,4],[0,0,3],[0,0,5]])) # testcase 619 / 627



if __name__ == '__main__':
    main()
