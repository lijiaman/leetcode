# 20ms(100%), 13.1M(83.69%)
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1_list = version1.split('.')
        v2_list = version2.split('.')
        v1_int_list = []
        v2_int_list = []
        for v1 in v1_list:
            v1_int_list.append(int(v1))
        for v2 in v2_list:
            v2_int_list.append(int(v2))

        for i in range(max(len(v1_int_list), len(v2_int_list))):
            v1 = v1_int_list[i] if i < len(v1_int_list) else 0
            v2 = v2_int_list[i] if i < len(v2_int_list) else 0
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1

        return 0
