def decimal_to_roman(number):
    roman_numerals = {
        1000: "M", 900: "CM", 500: "D", 400: "CD",
        100: "C", 90: "XC", 50: "L", 40: "XL",
        10: "X", 9: "IX", 5: "V", 4: "IV",
        1: "I"
    }
    
    roman_string = ""
    for value, numeral in roman_numerals.items():
        while number >= value:
            roman_string += numeral
            number -= value
    return roman_string

