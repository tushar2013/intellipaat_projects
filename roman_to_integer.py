class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }

        roman_num_list = []

        if 'IV' in s:
            roman_num_list.append(roman_num['IV'])
            s = s.replace('IV', '')
        if 'IX' in s:
            roman_num_list.append(roman_num['IX'])
            s = s.replace('IX', '')
        if 'XL' in s:
            roman_num_list.append(roman_num['XL'])
            s = s.replace('XL', '')
        if 'XC' in s:
            roman_num_list.append(roman_num['XC'])
            s = s.replace('XC', '')
        if 'CD' in s:
            roman_num_list.append(roman_num['CD'])
            s = s.replace('CD', '')
        if 'CM' in s:
            roman_num_list.append(roman_num['CM'])
            s = s.replace('CM', '')

        for char in s:
            roman_num_list.append(roman_num[char])
        return sum(roman_num_list)


solution = Solution()
print(solution.romanToInt('MCMXCIV'))
