class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = max(len(word) for word in words)

        ans = []

        for i in range(max_len):
            col = ""

            for word in words:
                if i < len(word):
                    col += word[i]
                else:
                    col += " "

            ans.append(col.rstrip())

        return ans               

        