class Solution:
    # やりたいことがわかりにくいので、NeetCodeの解説動画見るといい

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':  # jをデリミタ'#まで動かす
                j += 1
            length = int(s[i:j])  # iから'#'の手前までは、何文字の文字列がこの後来るかを表す
            res.append(s[j+1:j+1+length])
            i = j+1+length
        return res
