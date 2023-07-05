import sys

filename = sys.argv[1]

fr=open(filename,"r")
l = fr.read()

print(l)

fw = open("dst.txt","w")
fw.write(l)
fw.close
