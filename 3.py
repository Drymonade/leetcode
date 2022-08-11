class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}

        max_len = 0
        cur_len = 0

        for idx, ch in enumerate(s):
            if ch not in d:
                cur_len += 1
            else:
                if cur_len > max_len:
                    max_len = cur_len

                last_idx = d[ch]
                cur_len = idx - last_idx

                d = {}

                for j in range(last_idx + 1, idx):
                    d[s[j]] = j

            d[ch] = idx

        return max(max_len, cur_len)
