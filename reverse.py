def rem(string)
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in string.lower():
        if x in vowels:
            string = string.replace(x,"")
    print(string)
    return string
string = input("enter the word length:")
string = input("")
string = string[::-1]
rem(string)
