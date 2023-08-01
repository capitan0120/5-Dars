class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans = ''
        cur = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '-':
                continue

            ans += s[i].upper()
            cur += 1

            if cur == k and i:
                cur = 0
                ans += '-'

        return ans[::-1] if (ans and ans[-1]) != '-' else ans[::-1][1:]