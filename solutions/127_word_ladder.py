### Notice dequeue is much faster than list! with list as queue, got TLE!
# BFS
import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = collections.deque([beginWord])
        level = 1
        while len(queue) > 0:
            size = len(queue)
            level += 1
            for i in range(size):
                curr_w = queue.popleft()
                for j in range(len(curr_w)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new_w = curr_w[:j] + c + curr_w[j + 1:]
                        if new_w in wordList:
                            queue.append(new_w)
                            wordList.remove(new_w)
                            if new_w == endWord:
                                return level

        return 0
