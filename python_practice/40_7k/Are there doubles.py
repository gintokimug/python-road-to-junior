# Your job is to build a function which determines whether or not there are double characters in a string (including whitespace characters). For example aa, !! or   .

# You want the function to return true if the string contains double characters and false if not. The test should not be case sensitive; for example both aa & aA return true.

def double_check(strng):
    s = strng.lower()
    for x in range(len(strng)- 1):
        if s[x] == s[x + 1]:
            return True 
    else:
        return False 
        
example = "1334568"
print(double_check(example))

