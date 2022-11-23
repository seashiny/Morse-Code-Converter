# dictionary for mapping characters to morse code\\创建mapping dictionary
MORSE_ENCODING = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',

    '.': '.-.-.-', ':': '---...', ',': '--..--', ';': '-.-.-.',
    '?': '..--..', '=': '-...-', "'": '.----.', '/': '-..-.',
    '!': '-.-.--', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '(': '-.--.', ')': '-.- -.-', '$': '...-..-', '&': '....',
    '@': '.--.-.',
}

# reverse the mapping for decod\\通过dictionary comprehension转置mapping dictionary的key和value，为decoding做准备
MORSE_DECODING = {value: key for key, value in MORSE_ENCODING.items()}


def encode(message):
    code = ''
    # checking for space\\一个空格连接的字符，两个空格连接的单词
    # to add single space after every character and double space after every word
    for index, char in enumerate(message):
        if char == ' ':
            code += ' '
        else:
            # error handling
            try:
                code += MORSE_ENCODING[char.upper()]
            except KeyError:
                raise ValueError(f'Char "{char}" at {index} cannot be encoded.')
            code += ' '

    return print(code[:-1]) # 转化后的code结尾多出来一个空格，使用索引删除


def decode(morse_code):
    message = ''
    # split the code to translatable sequence\\通过分割成连续的可转换的sequence来简化操作
    for index, sequence in enumerate(morse_code.split(' ')):
        if sequence == '':
            message += ' '
        else:
            try:
                message += MORSE_DECODING[sequence]
            except KeyError:
                raise ValueError(f'Cannot decode code "{sequence} at {index}."')

    return print(message)

# 通过while循环控制应用运行和结束
should_end = False
while not should_end:
    operation = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if operation == 'encode':
        text = input("Type your message:\n")
        encode(text)
    elif operation == 'decode':
        text = input("Type your message:\n")
        decode(text)
    else:
        print('Please input valid text')

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
