import re
import glob

files = glob.glob("Testing\\ResearchArticles\\*.txt")
for fileName in files:
    theFile = open(fileName, 'r')
    fileString = theFile.read().replace('\n', ' ')
    theFile.close()
    newFile = open((fileName.replace('ResearchArticles', 'ResearchOutput')), 'w')
    newFile.write(fileString)
    newFile.close()
