import base64
import re

# ***** String to number ***** #
def str_to_num(string):
    number = 0
    for char in string:
        ascii_val = ord(char)
        number = (number << 8) | ascii_val
      
    return number
    
def num_to_str(num):
    string = ""
    while num != 0:
        ascii_val = num & 0xFF
        if not chr(ascii_val).isprintable():
            raise ValueError
            
        char = chr(ascii_val)
        string = char + string
        num = num >> 8
        
    return string
    
# ***** Base64 ***** #
def base64_encode(ascii_str):
    input_bytes = ascii_str.encode()
    output_bytes =  base64.b64encode(input_bytes)
    return output_bytes.decode()
    
def base64_decode(b64_str):
    input_bytes = b64_str.encode()
    output_bytes =  base64.b64decode(input_bytes)
    return output_bytes.decode()
    
# ***** Validators ***** #    
def is_base64(string):
    pattern = "\A[a-zA-Z0-9+/=]+\Z"
    result = re.match(pattern, string)
    return (result is not None)