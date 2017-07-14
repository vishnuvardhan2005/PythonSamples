from sys import argv

script, user_name = argv

prompt = '>'

print "Hi %s I'm the %s script" %(user_name, script)
print "Do you like me %s" % user_name
like = raw_input(prompt)

print "You have answered %s" % like
