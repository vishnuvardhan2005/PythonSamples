from sys import argv
from os.path import exists

script, source_file, dest_file = argv

print "Copying %s to %s" % (source_file, dest_file)

in_file = open(source_file)

indata = in_file.read()

print "Source file %d long" % len(indata)

print "Does the outfile exists? %s" % exists(dest_file)

raw_input(">")

out_file = open(dest_file, "w")

out_file.write(indata)

# close the files

in_file.close()
out_file.close()
