def restoreString(s, indices):
    """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        
    ans = []
    for i in sorted(indices):
        char = indices.index(i)
        ans.append(s[char])
    return ''.join(map(str, ans))


indic = [4, 5, 6, 7, 0, 2, 1, 3]

ans = restoreString("codeleet", indic)
print(ans)
