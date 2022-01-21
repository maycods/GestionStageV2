from django.shortcuts import render ,redirect
from .models import Encadreur, Stagiere
from satgesiV2.formEtud import  StagieresForm
from  satgesiV2.formEncadreur import EncadreurForm
from  satgesiV2.formPromoteur import PromoteurForm
# Create your views here.
def pageone (request):
 return render(request,'Firstpage.html')

def pagetwo (request):
 return render(request,'Secondpage.html')

def pagethree (request):
  return render(request,'thirdPage-GStage.html')

def pageacc (request):
    return render(request,'accept.html')

def pagefour (request):
    if request.method == "POST":
       form = StagieresForm(data=request.POST)
       if form.is_valid():
           form.save()
           return redirect("accept")
    else:
        formulaire = StagieresForm()
        return render(request,'fourthpage.html',{"formEtud":formulaire})

def pagefive (request):
    if request.method == "POST":
       form = PromoteurForm(data=request.POST)
       if form.is_valid():
           form.save()
           return redirect("accept")
    else:
        form = PromoteurForm()
        return render(request,'FivePage.html',{"formPromoteur":form})

def pagesix (request):
    if request.method == "POST":
       form = EncadreurForm(data=request.POST)
       if form.is_valid():
           form.save()
           return redirect("accept")
    else:
        formul = EncadreurForm()
        return render(request,'SixPage.html',{"formEncadreur":formul})

def boxstage (request):
 return render(request,'boxStage.html')

def Gencadreur (request): 
    Encadreurss = Encadreur.objects.all()
    return render(request,'Gencadreur.html', {'Ec':Encadreurss })

def boxstage2 (request):
 return render(request,'box2-Etudiant.html')

def Gstage (request):
 return render(request,'GStage.html')

def Gprom (request):
 return render(request,'Gpromoteur.html')

def Gstag (request):
 return render(request,'Gstagiare.html')

def GGstag (request):
 return render(request,'GGstagiare.html')

def Gtype (request):
 return render(request,'Gtypestage.html')

def Gorgan (request):
 return render(request,'Gorganime.html')

