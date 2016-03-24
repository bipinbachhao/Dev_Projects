from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)
print txt_again.read()

# Try something different here

first_file = txt.read()
second_file = txt_again.read()

print """
We are printing first file here:
%s
First file ends here.
--------------------------------
We are now printing Second file from here:
%s
Second file ends here.
""" % (txt.read(), second_file)
