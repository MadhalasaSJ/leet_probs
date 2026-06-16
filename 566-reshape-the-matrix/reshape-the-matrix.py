class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat

        nums = []
        for row in mat:
            nums.extend(row)

        res = []
        idx = 0

        for _ in range(r):
            res.append(nums[idx:idx +c])
            idx += c

        return res    
        