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


# Another solution that works and passes all tests.
# This is the solution CoPilot gave. I haven't studies this one yet.
def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
    n = len(nums)
    diff = [0] * (n + 1)
    sum_val = 0
    pos = 0

    for i in range(n):
        while sum_val + diff[i] < nums[i]:
            if pos == len(queries):  # All queries exhausted
                return -1

            start, end, val = queries[pos]
            pos += 1

            if end < i:  # Skip irrelevant updates
                continue

            # Apply range update in O(1)
            diff[max(start, i)] += val
            if end + 1 < n:
                diff[end + 1] -= val

        sum_val += diff[i]

    return pos


# another solution taht I came up with. Just practicing it to make sure I understand.
# 1.) All Testcases passed!
# 2.) Solution Accepted!
def minZeroArray(nums: list[int], queries: list[list[int]]) -> int:
    def nums_is_all_zero(n: int):
        diff = [0] * len(nums)

        for start, end, inc in queries[:n + 1]:
            diff[start] += inc
            if end + 1 < len(nums):
                diff[end + 1] -= inc 

        # prefix_sum(diff)
        for i in range(len(diff) - 1):
            diff[i + 1] += diff[i]

        for i in range(len(diff)):
            val = nums[i] - diff[i]
            if val <= 0:
                pass
            else:
                return False
        
        return True
    
    if sum(nums) == 0:
        return 0
    
    N = len(nums)
    Q = len(queries)

    left = 0
    right = Q - 1
    ans = -1
    first_pass = True

    while left <= right:
        middle = (left + right) // 2
        value = queries[middle]

        if nums_is_all_zero(middle):
            ans = middle + 1
            right = middle - 1
            if left == right:
                if first_pass:
                    first_pass = False
                else:
                    break
        else:
            left = middle + 1
            if left == right:
                if first_pass:
                    first_pass = False
                else:
                    break 
    
    return ans


def main() -> None:
    print(minZeroArray(nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]])) # 2
    print(minZeroArray(nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]])) # -1
    print(minZeroArray(nums = [0], queries = [[0,0,2],[0,0,4],[0,0,4],[0,0,3],[0,0,5]])) # testcase 619 / 627


if __name__ == '__main__':
    main()
