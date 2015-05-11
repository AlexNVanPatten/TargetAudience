import io
import csv

file1 = 'dogs.csv'
file2 = 'tweens.csv'
file3 = 'researchers.csv'


def readFile():

    list1 = []
    list2 = []
    list3 = []

    with open('dogs.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter='\n', quotechar='|')
        for row in reader:
            list1 = list1 + row

    with open('tweens.csv') as csvfile2:
        reader2 = csv.reader(csvfile2, delimiter='\n', quotechar="|")
        for row in reader2:
            list2 = list2 + row

    with open('researchers.csv') as csvfile3:
        reader3 = csv.reader(csvfile3, delimiter='\n', quotechar="|")
        for row in reader3:
            list3 = list3 + row

    return (list1, list2, list3)

readFile()
