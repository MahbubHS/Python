#!/usr/bin/env python3
# __Author__ : P-NP
# __Desc__   : None

import argparse

class EncrypterDecrypter:
    """
    Class for performing text encryption and decryption using a specified character set and shift value.
    """

    def __init__(self, character_set):
        """
        Initialize the EncrypterDecrypter instance with a character set.
        :param character_set: The set of characters to use for encryption and decryption.
        """
        self.character_set = character_set

    def encrypt(self, text, shift):
        """
        Encrypt the given text using the specified shift value.
        :param text: The text to encrypt.
        :param shift: The shift value.
        :return: The encrypted text.
        """
        encrypted_text = ""
        for char in text:
            if char in self.character_set:
                index = (self.character_set.index(char) + shift) % len(self.character_set)
                encrypted_text += self.character_set[index]
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, encrypted_text, shift):
        """
        Decrypt the given encrypted text using the specified shift value.
        :param encrypted_text: The text to decrypt.
        :param shift: The shift value.
        :return: The decrypted text.
        """
        decrypted_text = ""
        for char in encrypted_text:
            if char in self.character_set:
                index = (self.character_set.index(char) - shift) % len(self.character_set)
                decrypted_text += self.character_set[index]
            else:
                decrypted_text += char
        return decrypted_text

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Encrypter and Decrypter")
parser.add_argument("-t", "--text", required=True, help="Text to encrypt or decrypt")
parser.add_argument("-s", "--shift", type=int, required=True, help="Shift value")
parser.add_argument("-e", "--encrypt", action="store_true", help="Encrypt the text")
parser.add_argument("-d", "--decrypt", action="store_true", help="Decrypt the text")
args = parser.parse_args()

# Validate command-line arguments
if args.encrypt == args.decrypt:
    parser.error("Specify either --encrypt or --decrypt")

# Define character set
character_set = "_$_:++$,"

# Create an instance of the EncrypterDecrypter class
encrypter_decrypter = EncrypterDecrypter(character_set)

# Perform encryption or decryption based on the command-line arguments
if args.encrypt:
    result = encrypter_decrypter.encrypt(args.text, args.shift)
    action = "encrypted"
else:
    result = encrypter_decrypter.decrypt(args.text, args.shift)
    action = "decrypted"

# Print the result
print(f"{action.capitalize()} Text: {result}")
