romanToDecimal = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

def romanNumeralToDecimal(romanNumeral):
    sum = 0
    for i in range(len(romanNumeral) - 1):
        left = romanNumeral[i]
        right = romanNumeral[i + 1]
        if romanToDecimal[left] < romanToDecimal[right]:
            sum -= romanToDecimal[left]
        else:
            sum += romanToDecimal[left]
    sum += romanToDecimal[romanNumeral[-1]]
    return sum

romanNumber = input("Enter roman number:")
print("Decimal number is: " + str(romanNumeralToDecimal(romanNumber.upper())))
