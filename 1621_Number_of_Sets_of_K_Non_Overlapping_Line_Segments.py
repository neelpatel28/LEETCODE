class Solution(object):
    def numberOfSets(self, n, k):
        MOD = 10**9 + 7
        total_items = n + k - 1
        choose = 2 * k
        
        if total_items < choose:
            return 0
            
        if choose > total_items - choose:
            choose = total_items - choose
            
        numerator = 1
        denominator = 1
        
        for i in range(choose):
            numerator = (numerator * (total_items - i)) % MOD
            denominator = (denominator * (i + 1)) % MOD
            
        return (numerator * pow(denominator, MOD - 2, MOD)) % MOD
