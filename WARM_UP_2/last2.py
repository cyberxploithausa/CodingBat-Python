"""
QUESTION

Given a string, return the count of the 
number of times that a substring length 2 
appears in the string and also as the last 2 
chars of the string, so "hixxxhi" yields 1 
(we won't count the end substring).


last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2

"""

# s = 'axxxaaxx'
# if len(s) < 2:
#     print('0')
# last2 = s[len(s)-2:]
# c = 0
# for i in range(len(s)-2):
#     sub = s[i:i+2]
#     if sub == last2:
#         c += 1
# print(c)

def last2(str):
    if len(str) < 2:
        return 0
    last2 = str[len(str)-2:]
    c = 0
    for i in range(len(str)-2):
        sub = str[i:i+2]
        if sub == last2:
            c +=1
    return c