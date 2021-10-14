consonant=lambda ch:True if (('A'<=ch<='Z' or 'a'<=ch<='z') and ch not in 'aeiouAEIOU') else False
ch=input("Enter the character")
print(consonant(ch))
