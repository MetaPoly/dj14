from django.shortcuts import render
import operator, re

def count(request):
    return render(request, 'wordcount/word.html', {'counttext':'100'})

def word(request):
    words = request.GET['fulltext']
    words = re.sub(r"(\w*)\W*(\w*)", r"\1 \2", words)
    wordslist = words.split(" ")
    worddict = {}
    for word in wordslist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

    sortword = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'wordcount/count.html', {'word':words, 'len':len(wordslist), 'worddict':sortword})

def help(request):
    help_text = 'this is the help page'
    intruction = 'to use the count function, all you need to do is\n' \
                 'enter what ever you like into the text box and click count!'
    return render(request, 'wordcount/help.html', {'help_text':help_text, 'intruc': intruction})
