from sys import argv
from os.path import exists

script, source_file, dest_file = argv
in_file = open(source_file)
indata = in_file.read()
out_file = open(dest_file, "w")
out_file.write(indata)

# close the files
in_file.close()
out_file.close()
