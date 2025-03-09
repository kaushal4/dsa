class Solution:
    def intToRoman(self, num: int) -> str:
        sol = ""
        third_degree = num // 1000
        sol += "M" * third_degree
        # second
        second_degree = (num // 100) % 10
        if second_degree == 4:
            sol += "CD"
        elif second_degree == 9:
            sol += "CM"
        else:
            if second_degree - 5 >= 0:
                sol += "D"
                second_degree -= 5
            sol += ("C" * second_degree)
        # first 
        first_degree = (num // 10) % 10
        if first_degree == 4:
            sol += "XL"
        elif first_degree == 9:
            sol += "XC"
        else:
            if first_degree - 5 >= 0:
                sol += "L"
                first_degree -= 5
            sol += ("X" * first_degree)
        # zero
        zero_degree = (num) % 10
        if zero_degree == 4:
            sol += "IV"
        elif zero_degree == 9:
            sol += "IX"
        else:
            if zero_degree - 5 >= 0:
                sol += "V"
                zero_degree -= 5
            sol += ("I" * zero_degree)
        return sol