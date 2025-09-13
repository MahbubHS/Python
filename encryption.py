import random
import string

chars = " " + string.digits + string.ascii_letters +"@"+"#"+ "."+"_"+"-"+"'"+"\""

chars = list(chars)
key = chars.copy()
random.shuffle(key)

#print(chars)
#print(key)

#Encrypt

plain_text = input("Enter your text : ")
encrypted_text = ""

for letter in plain_text:
    index = chars.index(letter)
    encrypted_text += key[index]

print(f"Original text : {plain_text}")
print(f"Encrypted text : {encrypted_text}")