def read_binary_file_data(filename):
    fp = open(filename, 'rb')
    size = get_file_size(fp)
    data = bytearray(size)
    fp.readinto(data)
    fp.close()
    return data

def write_binary_file_data(filename, data):
    fp = open(filename, 'wb')
    fp.write(data)
    fp.close()
    
def get_file_size(fp):
    fp.seek(0, 2)  # jump to end
    size = fp.tell()
    fp.seek(0)
    return size