def disemvowel(string_):
    vowels_string = "aeiouAEIOU"
    for x in vowels_string:
        string_ = string_.replace(x,"")
    return(string_)
my_text = "moloko"
result = disemvowel(my_text)


print(disemvowel(result))