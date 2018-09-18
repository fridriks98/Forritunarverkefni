def get_digit(number, position):
    '''return digit at position in number, counting from right'''
    return number//(10**position)%10