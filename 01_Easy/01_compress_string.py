# Given a string lowercase alphabet 's', eliminate consecutive duplicate characters from the string and return it. 
# That is, if the list contains repeated characters, they should be replaced with a single character.
# The order of the elements should not be changed. 

pattern = "aaaaauuhhhhbggffaa"
def compress_string(pattern):
    letters = [pattern[0]]
    cons = False
    for i in range (1,len(pattern)):
        if pattern[i] in letters:
            if pattern[i-1] == pattern[i]:
                cons = True
            else:
                cons = False
                letters.append(pattern[i])
        else:
            letters.append(pattern[i])
    final = ''.join(letters)
    return final

print(compress_string(pattern))
