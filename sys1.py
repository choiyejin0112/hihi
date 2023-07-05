import sys
# print(sys.argv)
filename=sys.argv[1]
fr=open(filename, "r")
for line in fr:
    print(line, end="")
    
fr. close()

# for i in range(int(sys.argv[1])):
#     print(i, "Hello")
