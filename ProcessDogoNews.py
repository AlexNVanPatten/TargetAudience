import glob
import re
import GunningFog

#This file takes htm files from DogoNews and returns the article as
#a string.

#Takes a file and makes it into a string with no newlines.
def file_to_string(fileName):
    theFile = open(fileName, 'r')
    fileString = theFile.read().replace('\n', '')
    theFile.close()
    return fileString

#Function to take a htm file from Dogonews and returns only the
#article's contents
def remove_html(fileString):
    #Removes all html markups
    fileString = re.sub('<.*?>', '', fileString)
    #Removes uneccessary symbols
    fileString = fileString.replace('&nbsp;', "")
    fileString = fileString.replace('\t', " ")
    #Removes all text leading up to article
    #The last thing before all DogoNews articles is a link to a Word Search
    fileString = re.sub('.*?Word Search', "", fileString)
    #Removes all text after article
    #DogoNews ends all articles with a list of used resources
    fileString = re.sub('Resources:.*', "", fileString)
    return fileString

#Tests above function by printing the file's string and it's GunningFog index
def process_file(fileName):
    fileString = file_to_string(fileName)
    fileString = remove_html(fileString)
    print GunningFog.count(fileString)
    return fileString
    
#Takes all htm files in the DogoNews folder and outputs the string's
#As text files in the TweenTribuneOutput folder
def makeOutputStrings():
    files = glob.glob("Testing\\DogoNews\\*.htm")
    print files
    for inFile in files:
        fileName = inFile.replace('Testing\\DogoNews\\',  '')
        fileName = fileName.replace('.htm', '')
        fileString = process_file(inFile)
        newFileName = "Testing\\DogoNewsOutput\\" + fileName + ".txt"
        outFile = open(newFileName, 'w')
        outFile.write(fileString)
        outFile.close()

makeOutputStrings()
