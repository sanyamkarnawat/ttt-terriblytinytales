from django.shortcuts import render
from django.http import HttpResponse

import urllib.request, urllib.error, urllib.parse
import string


url = 'https://terriblytinytales.com/test.txt'
def read():
    response = urllib.request.urlopen(url)
    webContent = response.read()
    webContent=str(webContent).lower()

    #data filtering
    x= webContent.replace("\\n"," ").replace("\\x9911","").replace("\\x80","").replace("\\xe2","").replace("\\","").replace("\\t"," ")
    x = x.split()
    return x
#algo to calculate the most frequent words from ttt site
def algo(x,n): 
    dict = {} 
    count= 0
    for item in reversed(x): 
        dict[item] = dict.get(item, 0) + 1
    
    sort_orders = sorted(dict.items(), key=lambda x: x[1], reverse=True)

    return(sort_orders[0:n])
#will Take value from user from html from in n here

def home(request):
    return render(request, 'home.html')
#will Take value from user from html from in n here
def add(request):
    fileContent = read()
    n= request.GET["num"]
    n=int(n)
    res= algo(fileContent,n)
    uiResult = ''
    for item in res:
        uiResult += '<tr><td>'+item[0]+'</td><td>'+str(item[1])+'</td></tr>'
    return render(request, 'result.html',{'result': res})