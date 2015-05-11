import ReadFile
import glob

def createDictionary(bag,d):
	while (bag != ""):
		x = bag.find('=')
		w = bag[0:x]
		x += 1
		end = len(bag)
		bag = bag[x:end]
		y = bag.find(' ')
		f = s[0:y]
		if w in d:
			d[w] = d[w] + float(f)
		else:
			d[w] = float(f)
		y += 1
		end = len(bag)
		bag = bag[y:end]
	return d

def categoryDitionary(xs):
	z = len(xs)
	d = {}
	for x in xs:
		d = createDictionary(x,d)
	for y in d:
		y = math.log(y/z)
	return d


def makeWords(art, ds):
	words = [0.0, 0.0, 0.0]
	while (art != ""):
		x = art.find(' ')
		if x != -1:
			w = art[0:x]
			x += 1
			last = len(art)
			art = art[x,last]
		else:
			w = art
			art = ""
		if w != "-":
			w = w.replace('?', '').replace('!', '').replace(':','').replace(';', '').replace(',', '').replace('.', '').replace('"', '')
			if "'" in art:
				y = w.find("'")
				z = w[0:y]
				y += 1
				end = len(w)
				w = w[y:end]
				i = 0
				for d in ds:
					if z in d:
						words[i] = words[i] + d[z]
					i += 1
			if w != "":
				i = 0
				for d in ds:
					if w in d:
						words[i] = words[i] + d[w]
					i += 1
	return words


# 0 = Dogs, 1 = Tweens, 2 = Researchers
def classify(art, ds):
	values = makeWords(art,ds)
	i = 0
	win = 0
	pos = 0
	for x in values:
		if x > win:
			win = x
			pos = i
		i += 1
	return pos

#Gets Bag Strings, creates the three bags of words
def makeBags():
        BagStrings = ReadFile.readFile()
        BagDog = categoryDictionary(BagsString[0])
        BagTweens = categoryDictionary(BagsString[1])
        BagResearch = categoryDictionary(BagsString[2])
        return [BagDog, BagTweens, BagResearch]

def makeArticlesChoice(artNames):
        bags = makeBags()
        choices = []
        outFile = open("Testing\\TestingOutput\\ourChoices.txt", 'w')
        for name in artNames:
                article = open(name, 'r')
                fileString = theFile.read()
                winner = classify(fileString, bags)
                outFile.write(name + " classified as " + winner + "\n")
                choices = choices + winner
        return choices

def parsing():
        files = glob.glob("Testing\\TestingArticles\\*.txt")
        print(makeArticlesChoice(files))

parsing()
