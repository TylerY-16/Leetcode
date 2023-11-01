class Solution:
    def romanToInt(self, s: str) -> int:
        
        result = []
        for i in s:
            match i:
                case "I":
                    result.append(1)
                case "V":
                    result.append(5)
                case "X":
                    result.append(10)
                case "L":
                    result.append(50)
                case "C":
                    result.append(100)
                case "D":
                    result.append(500)
                case "M":
                    result.append(1000)
        result.append(0)
        rom_sum = 0
        i = 0
        while i < len(result)-1:
            if result[i] < result[i+1]:
                rom_sum += result[i+1] - result[i]
                i+=1
            else:
                rom_sum += result[i]
            i+=1
        return rom_sum
                
                