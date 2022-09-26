from django.shortcuts import HttpResponse
from django.shortcuts import render,redirect
from .forms import BrandForm
from .models import Brand


# Create your views here.
def Brand_list(request):
    context={'list':Brand.objects.all()}
    return render(request, "list.html",context)

def Brand_form(request,id=0):
    if request.method == "GET":
        if id==0:
            form=BrandForm()
        else:
            brand=Brand.objects.get(pk=id)  
            form=BrandForm(instance=brand)  
      
  
        return render(request,"form.html", {'form':form})
    elif request.method=='POST' :
        if id == 0:
            form=BrandForm(request.POST)
        else:
            brand=Brand.objects.get(pk=id)
            form=BrandForm(request.POST,instance=brand)    
        
        if form.is_valid():
            form.save()
        return redirect('/Brands')  




def Brand_delete(request,id):
    brand=Brand.objects.get(pk=id)
    brand.delete()
    return redirect('/Brands')



          


       