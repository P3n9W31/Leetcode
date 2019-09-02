class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash_5 = 0
        cash_10 = 0
        for bill in bills:
            if bill == 5:
                cash_5 += 1
            elif bill == 10:
                if cash_5 == 0:
                    return False
                else:
                    cash_5 -= 1
                    cash_10 += 1
            elif bill == 20:
                if cash_10 > 0:
                    if cash_5 > 0:
                        cash_10 -= 1
                        cash_5 -= 1
                    else:
                        return False
                else:
                    if cash_5 >= 3:
                        cash_5 -= 3
                    else:
                        return False
        return True
                    