import re
import GunningFog

#This file takes htm files from Philosophy Now and returns the article as
#a string.

#Takes a file and makes it into a string with no newlines.
def file_to_string(fileName):
    theFile = open(fileName, 'r')
    fileString = theFile.read().replace('\n', '')
    theFile.close()
    return fileString

#Function to take a htm file from Philosophy Now and return only the
#article's contents
def remove_html(fileString):
    #Removes everything leading up to the article
    #Philosophy Now uses h1 uniquely as the title for an article
    fileString = re.sub('.*?<h1>', "<h1>", fileString)
    #Removes all html markups
    fileString = re.sub('<.*?>', '', fileString)
    #Removes Various non-necessary symbols
    fileString = fileString.replace('&nbsp;', "")
    fileString = fileString.replace('\t', " ")
    fileString = fileString.replace('&lsquo;', "")
    fileString = fileString.replace('&rsquo;', "")
    fileString = fileString.replace('&rdquo;', "")
    fileString = fileString.replace('&ndash;', "")
    fileString = fileString.replace('&ndash;', "")
    fileString = fileString.replace('&amp;', "")
    fileString = fileString.replace('&copy;', "")
    #Removes everything after the article.
    #Philosophy Now has ABOUT as the first word after every article.
    fileString = re.sub('ABOUT.*', "", fileString)
    return fileString

#Tests above function by printing the file's string and it's GunningFog index
def process_file(fileName):
    fileString = file_to_string(fileName)
    fileString = remove_html(fileString)
    print fileString
    print GunningFog.count(fileString)
    
process_file("Testing\\PhilosophyNow\\hetfacebook.htm")
