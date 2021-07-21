"""
QUESTION

Given a non-empty string like "Code" 
return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'

"""

# y = "abc"
# return "".join([y[:i] for i in range(len(y) + 1)])

def string_splosion(str):
    return "".join([str[:i] for i in range(len(str) + 1)])
