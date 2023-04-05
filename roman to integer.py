roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
str1 = input("Enter the Roman value: ")
num = list(str1.upper())
total = 0

for i in range(len(num)):
    if num[i] in roman:
        if i < len(num) - 1 and roman[num[i]] < roman[num[i + 1]]:
            total -= roman[num[i]]
        else:
            total += roman[num[i]]
    else:
        print("Error: Invalid Roman numeral encountered -", num[i])

print("The equivalent value is", total)
