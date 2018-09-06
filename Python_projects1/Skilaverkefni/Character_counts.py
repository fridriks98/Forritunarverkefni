sentence = input(str("Enter a sentence: "))
Upper_case = 0
Lower_case = 0
number = 0
Punctuation = 0
space = 0

for i in range(len(sentence)):
    if sentence[i].isupper():
        Upper_case += 1
    elif sentence[i].islower():
        Lower_case += 1
    elif sentence[i].isdigit():
        number += 1
    elif sentence[i].isspace():
        space += 1        
    else:
        Punctuation += 1

print('{:>15s} {:>5d}'.format("Upper case",Upper_case))
print('{:>15s} {:>5d}'.format("Lower case",Lower_case))
print('{:>15s} {:>5d}'.format("Digits",number))
print('{:>15s} {:>5d}'.format("Punctuation",Punctuation))