#imported the modules from argv
from sys import argv

#uses the modules we imported
script, filename = argv

#opens the filename we put doesn't print out he text
txt = open(filename)

#prints out the file name using the formatter
print "Here's your file %s:" % filename

#prints out the the text within the code
print txt.read()

print "Type the filename again:"

file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt_again.close()
txt.close()

