import glob
import re
import GunningFog

#This file takes htm files from Tween Tribune and returns the article as
#a string.

#Takes a file and makes it into a string with no newlines.
def file_to_string(fileName):
    theFile = open(fileName, 'r')
    fileString = theFile.read().replace('\n', '')
    theFile.close()
    return fileString

#Function to take a htm file from Tween Tribune and returns only the
#article's contents
def remove_html(fileString):
    #Removes all html markups
    fileString = re.sub('<.*?>', '', fileString)
    fileString = fileString.replace('\t', " ")
    #Removes everything leading up to article
    #Tween Tribune has the words Associated Press before every article
    fileString = re.sub('.*?Associated Press', "", fileString)
    #Removes everything after the article
    #Tween Tribune ends every article with a Critical Thinking Challenge
    fileString = re.sub('Critical thinking challenge.*', "", fileString)
    return fileString

#Tests above function by printing the file's string and it's GunningFog index
def process_file(fileName):
    fileString = file_to_string(fileName)
    fileString = remove_html(fileString)
    print GunningFog.count(fileString)
    return fileString

#Takes all htm files in the TweenTribune folder and outputs the string's
#As text files in the TweenTribuneOutput folder
def makeOutputStrings():
    files = glob.glob("Testing\\TweenTribune\\*.htm")
    for inFile in files:
        fileName = inFile.replace('Testing\\TweenTribune\\',  '')
        fileName = fileName.replace('.htm', '')
        fileString = process_file(inFile)
        newFileName = "Testing\\TweenTribuneOutput\\" + fileName + ".txt"
        outFile = open(newFileName, 'w')
        outFile.write(fileString)
        outFile.close()

makeOutputStrings()
    
