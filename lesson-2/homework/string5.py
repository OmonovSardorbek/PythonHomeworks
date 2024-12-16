user_input = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowels_count = 0
consonant_count = 0
for i in user_input:
    if i in vowels:vowels_count+=1
    if i not in vowels:consonant_count+=1

print(f"Vowels: {vowels_count}, Consonants: {consonant_count}")