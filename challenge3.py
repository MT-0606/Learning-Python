# CHALLENGE #3: Determine whether a string is a palindrome.

def is_palindrome(string):
    # Basically, a palindrome is a string that reads the same forwards
    # and backwards.

    # 1. Ignore capitalisation, non-alphanumeric values, and spaces.
    string1 = string.lower()
    string2 = ''.join(char for char in string1 if char.isalnum())
    print(string2)

    # 2. Check whether all characters at both ends of the string
    #    are the same.
    flag = False # default value
    len_string = len(string2)
    for i in range(0,len_string):
        if (string2[i]==string2[-i]):
            flag = True
        else:
            flag = False
            break
        
    return flag
    

test = "RACECAR"

result = is_palindrome(test)
print(result)
