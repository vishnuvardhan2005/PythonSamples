from sys import argv

script, fileName = argv

txt = open(fileName)

print "Here's is your file %r" % fileName

print txt.read()

print "Give another file name:"
fileName = raw_input('> ')
txt = open(fileName)

print txt.read()

fileName.close()
