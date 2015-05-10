import io
import csv

file1 = 'dogs.csv'
file2 = 'tweens.csv'
file3 = 'researchers.csv'

list1 = []
list2 = []
list3 = []

def readFile:

    with open('dogs.csv', newline='\n') as csvfile:
        reader = csv.reader(csvfile, quotechar='|')
        for row in reader:
            list1 = list1 + row

    with open('tweens.csv', newline='\n') as csvfile2:
        reader2 = csv.reader(csvfile, quotechar="|")
        for row in reader:
            list2 = list2 + row

    with open('researchers.csv', newline="\n") as csvfile3:
        reader3 = csv.reader(csvfile, quotechar="|")
        for row in reader:
            list3 = list3 + row

    return (list1, list2, list3)


