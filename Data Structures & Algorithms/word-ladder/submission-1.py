class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        if endWord not in wordset:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            word, hop = queue.popleft()
            if word == endWord:
                return hop

            word = list(word)
            for i in range(len(word)):
                orig_letter = word[i]
                for j in "abcdefghijklmnopqrstuvwxyz":
                    word[i] = j
                    new_word = "".join(word)
                    if new_word in wordset:
                        queue.append((new_word, hop+1))
                        wordset.remove(new_word)
                word[i] = orig_letter

        return 0