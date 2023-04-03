def sort_two_strings(word1, word2):
    changeword = word1
    if word1 < word2:
        return word1 + " " + word2
    else:
        word1 = word2
        word2 = changeword
        return word1 + " " + word2


print(sort_two_strings("Lovelace", "Byron"))