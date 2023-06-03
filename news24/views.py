from django.shortcuts import render,redirect
from .models import contact, news

def index(request):
    page = news.objects.all()
    return render(request, 'index.html', {"page":page})

def contactsave(request):
    if "submit" in request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        new_contact = contact(name=name, email=email, subject=subject, meassage=message)
        print(new_contact,"aaa")
        new_contact.save()
        new_contact.refresh_from_db()
        
    return render(request, 'contact.html', )
def contactlist(request):
    ct = contact.objects.all()
    print(ct, "aaaa")
    return render(request, 'new.html', {"ct":ct})

def uploaddata(request):
    if request.method =="POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        obj = contact(name=name, email=email, subject=subject,message=message)
        if obj.is_valid():
            cd = obj.cleaned_data
            cd.save()
        return redirect("contact")
    return render(request, 'contact.html')

def sports(request):
    page = news.objects.all()
    return render(request, 'sports.html', {"page":page})
    # return render(request, 'sports.html')

def tech(request):
    page = news.objects.all()
    return render(request, 'tech.html', {"page":page})

def fashion(request):
    page = news.objects.all()
    return render(request, 'fashion.html', {"page":page})

def latestnews(request):
    page = news.objects.all()
    return render(request, 'news.html' , {"page":page})
def home(request):
    page = news.objects.all()
    return render(request, 'index.html' , {"page":page})