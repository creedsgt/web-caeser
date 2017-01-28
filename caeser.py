abc = "abcdefghijklmnopqrstuvwxyz"
def alphabet_position(achar):
    return abc.index(achar.lower())



def rotate_character(achar, rot):
    char = abc[(alphabet_position(achar) + int(rot)) % 26]
    if achar.isupper():
        return char.upper()
    else:
        return char.lower()
    return  char

def encrypt(message, rot):
    line = ""
    for new_char in message:
        if new_char.isalpha():
        	line = line + rotate_character(new_char, rot)
        else:
            line = line + new_char
    return line
