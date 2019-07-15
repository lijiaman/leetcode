## Need to optimize!

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [0] * len(gas)
        for i in range(len(gas)):
            diff[i] = gas[i] - cost[i]
        for k in range(len(gas)):
            if diff[k] >= 0:
                cnt = 0
                flag = True
                for j in range(k, len(diff)):
                    cnt += diff[j]
                    if cnt < 0:
                        flag = False
                        break
                if k > 0:
                    for j in range(0, k):
                        cnt += diff[j]
                        if cnt < 0:
                            flag = False
                            break
                if flag:
                    return k

        return -1

