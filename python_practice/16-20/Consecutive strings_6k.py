def longest_consec(strarr, k):
    longest_word = ""
    n = len(strarr)

    if n == 0 or k > n or k <= 0:
        return ""
         
    for index in range(n - k + 1):
        current = "".join(strarr[index : index + k])

        if len(current) > len(longest_word):
            longest_word = current 

    return longest_word



def longest_consec(strarr, k):
    result = ""
    
    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index+k])
            if len(s) > len(result):
                result = s
            
    return result






print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
        
