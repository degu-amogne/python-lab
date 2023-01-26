
tallies = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    # specify more numerals if you wish
}

def RomanToDecimal(romanNumeral):
    sum = 0
    for i in range(len(romanNumeral) - 1):
        left = romanNumeral[i]
        right = romanNumeral[i + 1]
        if tallies[left] < tallies[right]:
            sum -= tallies[left]
        else:
            sum += tallies[left]
    sum += tallies[romanNumeral[-1]]

    if sum >3999:
        return print("Number is greater than 3999 or in appropriate!")
    else:
        return sum

print("-----------------------------------------------------------")
print("THIS PROGRAM CONVERTS ROMAN NUMBERS INTO DECIMAL NUMBERS!")
print("'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000,")
print("-----------------------------------------------------------")
while 1:
    try: 
        print("Enter any roman number from 1 to 3999")
        roman = input()
        if len(roman) <= 3:
            print(RomanToDecimal(roman))
        else:
            for i in range(len(roman) - 1):
                if roman[i] and roman[i+1] and roman[i+2] == roman[i+3]:
                    print("Please enter appropriate Roman number")
                    break
                else:
                    print(roman," = ",RomanToDecimal(roman))
        continue
    except:
        print("Error, Please give roman number only by using I,V,X,L,C,D,M")
    finally:
        print("------------------------------------------------------------")

