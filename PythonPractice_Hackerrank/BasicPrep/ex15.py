from sys import argv
script, filename = argv

txt = open(filename)

print("Content from file {0} is {1}".format(filename,txt.read()))
