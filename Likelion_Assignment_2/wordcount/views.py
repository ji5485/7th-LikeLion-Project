from django.shortcuts import render, redirect
import re

# Create your views here.

def main(request):
  return render(request, 'main.html')

def about(request):
  return render(request, 'about.html')

def result(request):
  if request.method == "POST":
    words = request.POST['words']
    wordDict = {}

    for word in words.split():
      parse = re.sub("""[.!?,"'~/<>]""", "", word)

      if wordDict.get(parse):
        wordDict[parse] += 1
      else:
        wordDict[parse] = 1

    return render(request, 'result.html', { 'words': words ,'wordDict': wordDict, 'wordCount': sum(wordDict.values()) })
  else:
    return redirect('main')