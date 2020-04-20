import base64
import random
import re

# ***** Strings ***** #
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
        char = chr(ascii_val)
        if not char.isprintable():
            raise ValueError
            
        string = char + string
        num = num >> 8
        
    return string
    
def extract_x_y(coord_pair):
    coords = coord_pair.split(',')
    if len(coords) != 2:
        raise ValueError
    return (int(coords[0]), int(coords[1]))
    
# ***** Base64 ***** #
def base64_encode(ascii_str):
    input_bytes = ascii_str.encode()
    output_bytes =  base64.b64encode(input_bytes)
    return output_bytes.decode()
    
def base64_decode(b64_str):
    input_bytes = b64_str.encode()
    output_bytes =  base64.b64decode(input_bytes)
    return output_bytes.decode()
    
def is_base64(string):
    pattern = "\A[a-zA-Z0-9+/=]+\Z"
    result = re.match(pattern, string)
    return (result is not None)
    
# ***** Bytes ***** #
def rand_xor_bytes(data, seed):
    result = bytearray(len(data))
    random.seed(seed)
    
    for index, byte in enumerate(data):
        xor_val = random.randint(0, 255)
        new_byte = byte ^ xor_val
        result[index] = new_byte
        
    return result
