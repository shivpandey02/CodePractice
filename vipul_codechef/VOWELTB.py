def is_vowel(char):
    if char in ['a', 'e', 'i', 'o', 'u']:
        return 'Vowel'
    else:
        return 'Consonant'
        
n = input().lower()
print(is_vowel(n))
