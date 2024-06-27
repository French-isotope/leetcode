def roman_to_int(s: str) -> int:
    roman_values =   {
                        'I' : 1,
                        'V' : 5,
                        'X' : 10,
                        'L' : 50,
                        'C' : 100,
                        'D' : 500,
                        'M' : 1000,
                     }
    previous_value = 0
    result = 0
    for letter in s:
        value = roman_values[letter]
        if value > previous_value:
            result += value - 2 * previous_value
        else:
            result += value
        previous_value = value
    return result


print(roman_to_int('III'))
print(roman_to_int('LVIII'))
print(roman_to_int('MCMXCIV'))


