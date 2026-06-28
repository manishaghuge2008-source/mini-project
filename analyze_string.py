def analyze_string(s):
    # Check empty string
    if s == "":
        print("String is empty!")
        return

    # Length of string
    print("Length of string:", len(s))

    # Reverse string
    print("Reversed string:", s[::-1])

    # Count vowels
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    print("Number of vowels:", count)

    # Print each character with index
    print("Characters with index:")
    for i in range(len(s)):
        print("Index", i, ":", s[i], " | Negative Index:", i - len(s))


# Take user input
user_input = input("Enter a string: ")

# Call function
analyze_string(user_input)