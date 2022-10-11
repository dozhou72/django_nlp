from django.http import HttpResponse
from django.shortcuts import render
import textblob
def home(request):
    return render(request,"home.html")
def result(request):
    lis=[]
    lis.append(request.GET["Text"])

       
    ans=textblob.TextBlob(lis[0]).sentiment.polarity
    return render(request,'result.html',{'ans':[ans]})
