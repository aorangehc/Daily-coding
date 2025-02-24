func wordBreak(s string, wordDict []string) bool {
	// dp[i]表示到当前字符串，是否可以成功拼接
	// 单词 word，长度为m，从当前位置向前截出长度为m的子串，如果匹配dp[i] = dp[i - m]
	// dp[0] = true
	n := len(s)
	dp := make([]bool, n+1)
	dp[0] = true

	for i := 1; i <= n; i++ {
		for _, word := range wordDict {
			lenWord := len(word)
			if lenWord <= i {
				subStr := s[i-lenWord : i]
				// fmt.Println(i, lenWord, word, subStr)
				if subStr == word {
					if dp[i] == false {
						dp[i] = dp[i-lenWord]
					}
				}
				//fmt.Println(i, lenWord, word, subStr, dp[i])
			}
		}
	}

	return dp[n]

}