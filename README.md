# TargetAudience

Classifies which of three sites an aritcle came from using a bag of words generated in Orange, and processed in the Parsing.py file. It classifies articles from DogoNews (kids news sources), TweenTribune (teen news source) and research articles. 

To do so, create a folder called Testing, and inside of it create a folder called TestingArticles, in which put the text version of all the articles you which to classify. The output of all files in TestingArticles will be created in a folder TestingOutput, ourChoices.txt. Articles classified as 0 are DogoNews, 1 are TweenTribune, and 2 are ResearchArticles.This is achieved by running Parsing.py.

This performs relatively well. It will sometimes misclassify a DogoNews aritcle as a research article (as it turns out, the aritcles written for kids are surprisingly complex, especially when comapred with the articles written for teens).

The various other files in here do things such as take an HTM file from DogoNews, and strip it down to just the article text. (ProcessDogoNews). 
