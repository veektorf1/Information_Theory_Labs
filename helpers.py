import random 

def get_histogram(input_file):
    dict_letters = dict()
    with open(input_file,"r") as file:
        for line in file:
            for char in line:
                if dict_letters.get(char)==None:
                    dict_letters[char] = 1
                else:
                    dict_letters[char]+=1
    return dict_letters

def get_array(hist):
    arr = []
    for key,value in hist.items():
        for _ in range(value):
            arr.append(key)
    return arr

def generate_random_letters(input_file, output_file,num):
    hist = get_histogram(input_file)
    # alphabet = list(hist.keys())
    rand_arr = get_array(hist)
    n = len(rand_arr)
    print(rand_arr)

    with open(output_file,'w') as file:
        for _ in range(num):
            rand_idx = random.randint(0,n-1)
            file.write(rand_arr[rand_idx])
    return None 

###############################################################
###############################################################
###############################################################

def print_matrix(dict_matrix):
    keys = dict_matrix.keys()
    print("-"*30)
    for key in keys:
        print(f'{key} | {dict_matrix[key]}')

    print("-"*30)
def get_histogram_matrix(input_file : str):
    '''
        For each letter calculates occurences of the subsequent letter 

        1st dimension dict -> last char
        2nd dimension dict -> current char

        Returns: 2D dict with counts
    '''
    dict_prev_letters = dict()

    with open(input_file,"r") as file:
        first_char = file.read(1)
        last_char = first_char

        for line in file:
            for char in line:
                if dict_prev_letters.get(last_char) == None:
                    dict_prev_letters[last_char] = dict()
                    dict_prev_letters[last_char][char] = 1
                else:
                    if dict_prev_letters[last_char].get(char) == None:
                        dict_prev_letters[last_char][char] = 1
                    else:
                        dict_prev_letters[last_char][char] +=1
                last_char = char
                # print(char,end=' ')
        return dict_prev_letters

   

def genRandomLetters(inputFile,n):
    '''
        @inputFile -> url for the alphabet
        @n -> number of letters
    '''
    dict_matrix = get_histogram_matrix(inputFile)
    
    #randomise first letter
    keys = list(dict_matrix.keys())
    last_char = keys[random.randint(0,len(keys)-1)]

    # 2,3,4,...n letter draw from the dict based on probability 
    for _ in range(1,n):
        subsq_keys = list(dict_matrix[last_char].keys())
        subsq_values =  list(dict_matrix[last_char].values())
        last_char = random.choices(subsq_keys,subsq_values)[0]
        print(last_char,end='')
    return
