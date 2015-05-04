import glob
import re

files = glob.glob("Testing\\DogoNewsOutput\\*.txt")
outFile = open("hatred.tab", 'w')
outFile.write("type\ttext\nchildren\tadult\tstring\nclass\n")
for inFile in files:
    theFile = open(inFile, 'r')
    fileString = theFile.read()
    outFile.write("Dogs\t")
    outFile.write(fileString)
    outFile.write("\n")

files2 = glob.glob("Testing\\TweenTribuneOutput\\*.txt")

for inFile in files2:
    theFile = open(inFile, 'r')
    fileString = theFile.read()
    outFile.write("Tweens\t")
    outFile.write(fileString)
    outFile.write("\n")
