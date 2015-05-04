import glob
import re

#Combines all articles into a tab deliniated text file for processing
#using orange.

outFile = open("CombinedArticles.tab", 'w')

#Dogonews, tagged Dogs
files = glob.glob("Testing\\DogoNewsOutput\\*.txt")
outFile.write("type\ttext\nTweens Dogs\tstring\nclass\n")
for inFile in files:
    theFile = open(inFile, 'r')
    fileString = theFile.read()
    outFile.write("Dogs\t")
    outFile.write(fileString)
    outFile.write("\n")

#Tween Tribune, tagged Tweens
files2 = glob.glob("Testing\\TweenTribuneOutput\\*.txt")
for inFile in files2:
    theFile = open(inFile, 'r')
    fileString = theFile.read()
    outFile.write("Tweens\t")
    outFile.write(fileString)
    outFile.write("\n")

#Research Articles, tagged Researchers
files3 = glob.glob("Testing\\ResearchOutput\\*.txt")
for inFile in files3:
    theFile = open(inFile, 'r')
    fileString = theFile.read()
    outFile.write("Researchers\t")
    outFile.write(fileString)
    outFile.write("\n")
