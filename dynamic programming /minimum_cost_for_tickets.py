# 983. Minimum Cost For Tickets
# Topics: Array, Dynamic Programming


class Solution:
    def minimun_cost_tickets(self, days: list[int], costs: list[int]) -> int:
        dp = [0] * (days[-1] + 1)
        for i in range(1, days[-1] + 1):
            if i not in days:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[max(0, i - 1)] + costs[0], dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2])
        return dp[-1]
        
