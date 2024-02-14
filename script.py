
def is_triangular(num):
    if num <= 0: 
        return False
    n = (-1+ (1 + 8* num) ** 0.5) / 2 
    return n.is_integer()

def decode(file_path):
    with open(file_path, 'r') as file: 
        lines = file.readlines()
    
    number_to_word = {}
    
    for line in lines:
        number, word = line.strip().split()
        number_to_word[int(number)] = word
    
    decoded_message = []
    
    for i in sorted(number_to_word.keys()):
        if is_triangular(i):
            decoded_message.append(number_to_word[i])
    
    return ' '.join(decoded_message)