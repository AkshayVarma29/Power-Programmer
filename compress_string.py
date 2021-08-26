# Given a string lowercase alphabet 's', eliminate consecutive duplicate characters from the string and return it. 
# That is, if the list contains repeated characters, they should be replaced with a single character.
# The order of the elements should not be changed. 

# Check the time taken for the program to run.
import time
start_time = time.time()

# Actual Code
s = "aaaaauuhhhhbggffaa"
def compress_string(s):
    letters = [s[0]]
    cons = False
    for i in range (1,len(s)):
        if s[i] in letters:
            if s[i-1] == s[i]:
                cons = True
            else:
                cons = False
                letters.append(s[i])
        else:
            letters.append(s[i])
    final = ''.join(letters)
    return final

print(compress_string(s))

# Print time taken
print("Process finished --- %s seconds ---" % (time.time() - start_time))
