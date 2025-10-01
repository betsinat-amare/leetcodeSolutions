class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        total = numExchange
        while total >= numExchange:
            qoutient = numBottles // numExchange
            reminder = numBottles % numExchange
            total = qoutient + reminder
            numBottles = total
            result += qoutient

        return result