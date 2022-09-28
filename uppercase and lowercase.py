def Count(str):
    upper, lower, number, special = 0, 0, 0, 0
    for i in range(len(str)):
        if str[i].isupper():
            upper += 1
            if str[i].islower():
                lower += 1
                if str[i].isdigit():
                    number += 1
                    if special == 1:
                    print('Upper case letters:', upper)
                    print('Lower case letters:', lower)
                    print('Number:', number)
                    print('Special characters:', special)
                    str =input("enter the string")
                    Count(str)
