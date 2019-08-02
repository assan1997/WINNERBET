from django.http import Http404
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    return render(request, 'app/acceuil.html',{'match':request.session['match']})

def ang(request):
   
    return render(request ,'app/pl.html')

@csrf_exempt
def add(request):
    request.session['match']=''
    request.session['prono']=''
    request.session['cote']=''
    data={}
    somme=[]
    if request.method=='POST': 
        if request.session:
            if len(request.session['match'])<=14:
                request.session['match']+=request.POST['match']
                request.session['prono']+=request.POST['prono']
                request.session['cote']+=request.POST['cote']
                match =request.session['match']
                prono =request.session['prono']
                cote=request.session['cote']
        data={
            'match':match,
            'prono':prono,
            'cote':cote,
        }
    return JsonResponse(data)


