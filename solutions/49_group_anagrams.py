def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    str_dict = {}
    for str in strs:
        list_k = [0] * 26
        for chr in str:
            list_k[ord(chr) - ord('a')] += 1
        if tuple(list_k) in str_dict:
            str_dict[tuple(list_k)].append(str)
        else:
            str_dict[tuple(list_k)] = []
            str_dict[tuple(list_k)].append(str)

    return str_dict.values()
