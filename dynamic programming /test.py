s = "leetcode"
word_dict = ["leet","code"]
dp = [False] * (len(s) + 1)
dp[len(s)] = True
for i in range((len(s) - 1), -1, -1):
    for word in word_dict:
        if i + len(word) <= len(s) and s[i: i + len(word)] == word:
            dp[i] = dp[i + len(word)]
        if dp[i]:
            break
print(dp[0])

def multiply_two_number()