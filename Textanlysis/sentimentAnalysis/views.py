from django.shortcuts import render, redirect
from .sentiment_analysis import analyze_sentiment
from .models import save_result
from django.contrib.auth.decorators import login_required



def homePage(request):
    return render(request, 'home.html')

@login_required
def inputFromUser(request):
    if request.method == 'POST':
        text = request.POST['text']
        return redirect('sentimentAnalysisResult', text=text)
    return render(request,'inputUser.html') 

@login_required
def sentimentAnalysisResult(request,text):

   sentiment, confidence= analyze_sentiment(text)
   context={
            'text': text,
            'sentiment': sentiment,
            'confidence': confidence,
        }
   print(request.user)
   SaveResult = save_result(user=request.user,text=text,sentiment=sentiment,confidence=confidence)
   SaveResult.save()

   return render(request,'result.html',context)

@login_required   
def history(request):
    results = save_result.objects.filter(user=request.user)
    context = {
        'results': results
    }

    return render(request, 'History.html',context)
