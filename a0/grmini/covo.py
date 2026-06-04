s = "humain ti"
vowels = 0
consonants = 0

for char in s:
    if char in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1
        
print(f"bh: {vowels}, ha: {consonants}")