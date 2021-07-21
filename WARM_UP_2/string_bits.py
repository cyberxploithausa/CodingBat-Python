"""
QUESTION


Given a string, return a new string made 
of every other char starting with the 
first, so "Hello" yields "Hlo".


string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'

"""
# s = 'hello'
# print(s[0::2])

def string_bits(str):
    return (str[0::2])