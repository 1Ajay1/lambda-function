consonant=lambda ch: "consonant" if ch not in 'aeiouAEIOU' else "Vowel"
ch=input("Enter the alphabet character")
print(consonant(ch))
