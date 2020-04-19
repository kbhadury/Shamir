MAIN_MENU_HEADER = """
****************************************
            Select an option
Encrypt a message......................1
Decrypt a message......................2
Encrypt a file.........................3
Decrypt a file.........................4
Modify an encrypted file...............5
Exit...................................0
"""

MAIN_MENU_FOOTER = """
****************************************
"""

ENCRYPTION_INSTRUCTIONS = """
****************************************
This program allows you to encrypt a    
secret message.  To decrypt it, two keys
must be provided to decrypt.py.  You can
generate as many keys as you want.
****************************************
"""

ENCRYPTION_FOOTNOTE = """
Remember, any two of these keys can be used to decrypt your secret message.
However, this means you can hand out one key to each person and they won't
be able to decrypt your message without knowing someone else's key.    

These keys must be kept private by their owners.
"""

DECRYPTION_INSTRUCTIONS = """
****************************************
This program allows you to decrypt a
secret message that was encrypted using
encrypt.py.  You must have two keys
associated with the secret.
****************************************
"""

DECRYPTION_ERROR_MESSAGE = "Error: message could not be decrypted."

NUM_SLOPE_DIGITS = 20