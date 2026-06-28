def analyze_string(s):
    
    if s == "":
        print("String is empty!")
        return

    
    print("Length of string:", len(s))

    
    print("Reversed string:", s[::-1])

    
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    print("Number of vowels:", count)

    
    print("Characters with index:")
    for i in range(len(s)):
        print("Index", i, ":", s[i], " | Negative Index:", i - len(s))



user_input = input("Enter a string: ")


analyze_string(user_input)
