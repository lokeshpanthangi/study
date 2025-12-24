# Problem 3: The "Raw" Signal Check

# Scenario: A military device receives encrypted messages. Before decoding, you need to check if the message is "symmetric".

# Requirement: A message is considered symmetric if, after converting all uppercase letters into lowercase letters and removing 
# all non-alphanumeric characters (like spaces, commas, symbols), it reads the same forward and backward.

# Input: "A man, a plan, a canal Panama"

# Expected Output: True


##### SOLUTION #####

# SO in the following solution we just have to check string reverse is the same or not but in the string we have so many caps and unwanted chars
# GOTTA REMOVE EM 

s = "A man, a plan, a canal : Panamaz"

def fun3(s):
    s1 = ''
    for i in s:
        if i.isalpha():
            s1+=i
    s1 = s1.lower()
    if s1 == s1[::-1]:
        return True
    return False

result = fun3(s)
print(result)

