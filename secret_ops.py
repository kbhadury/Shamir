import data_ops
import secrets
import string

def generate_keys(secret_num, num_keys, slope_size):
    slope = get_rand_num(slope_size)
    keys = []
    for i in range(num_keys):
        x_pos = i + 1
        key_val = secret_num + slope*x_pos
        key = str(x_pos) + ',' + str(key_val)
        keys.append(data_ops.base64_encode(key))
        
    return keys
    
def get_secret_num(key_1, key_2):
    key_1_coords = data_ops.base64_decode(key_1)
    key_2_coords = data_ops.base64_decode(key_2)
    
    x_1, y_1 = data_ops.extract_x_y(key_1_coords)
    x_2, y_2 = data_ops.extract_x_y(key_2_coords)
    
    secret_num = solve_for_intercept(x_1, y_1, x_2, y_2)
    return secret_num
    
def get_rand_num(num_digits):
    num_str = ''.join(secrets.choice(string.digits) for i in range(num_digits))
    return int(num_str)
    
def solve_for_intercept(x_1, y_1, x_2, y_2):
    slope = (y_2 - y_1) // (x_2 - x_1)
    intercept = y_1 - slope*x_1
    return intercept
