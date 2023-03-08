from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import LongToShort

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello Me!")

def task(request):
    context={"year": "2023", "attendees": ["Adi", "R", "T", "S"]}
    return render(request, "task.html", context)

def home_page(request):
    context={"submitted": False}
    context={"error": False}
    if request.method=="POST":
        #print(request.POST)
        data=request.POST
        long_url=data['longurl']
        custom_name=data['custom_name'] 
        try:
            context["long_url"]=long_url
            context["custom_name"]=request.build_absolute_uri() + custom_name
                #request.build_absolute_uri() gives current url so, context["custom_name"]--> http://127.0.0.1:8000/custom_name

            #obj me left side wala long_url yha ke variables hain, right side ka long_url models ke variables hain
            obj=LongToShort(long_url=long_url, custom_name=custom_name)

            print(long_url, custom_name)
            obj.save()
            
            context["submitted"]=True
            context["date"]=obj.created_Date
            context["clicks"]=obj.visit_count
            print(context["submitted"], context["date"], context["clicks"])
        except:
            context["error"]=True       #to prevent from going to new page
    else:
        print("User request not submitted")
    return render(request, "index.html", context)

def redirect_url(request, custom_name):
    #return HttpResponse(custom_name)
    row=LongToShort.objects.filter(custom_name=custom_name)     #retrieve some objects from database jaha ye condition satisfy ho
                    #left wala custom_name model ka hai, right wala custom name slug se aarha hai
                    #row is an object
    print(row)

    #aisa endpoint jo hmne insert hi nhi kiya
    if len(row)==0:
        return HttpResponse("This Endpoint does not exist")
    obj=row[0]          #phla object of model from rows
    long_url=obj.long_url
    obj.visit_count=obj.visit_count+1
    obj.save()
    return redirect(long_url) 

def analytics(request):
    rows=LongToShort.objects.all()  #database ke saare objects retrieve kro
    context={
        "rows":rows
    }
    return render(request, "analytics.html", context)

