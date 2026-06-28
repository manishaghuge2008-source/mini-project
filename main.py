def analyze_string(s):

    if s == "":
        print("String is empty")
        return


    print("Length of string:", len(s))


    print("Reverse string:", s[::-1])

    vowels = "aeiou"
    count = 0

    for ch in s.lower():
        if ch in vowels:
            count += 1

    print("Number of vowels:", count)

    print("Characters with index:")

    for i in range(len(s)):
        print("Positive index:", i, 
              "Negative index:", i-len(s), 
              "Character:", s[i])



string = input("Enter a string: ")


analyze_string(string)