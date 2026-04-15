class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        
        for i in range(len(operations)):
            op = operations[i]
            if op == "+":
                prevSum = res[-1] + res[-2]
                res.append(prevSum)
            elif op == "D":
                print(res)
                double = res[-1] * 2
                res.append(double)
            elif op == "C":
                res.pop()
            else:
                res.append(int(op))
        
        total = 0
        for n in res:
            total += n
        return total