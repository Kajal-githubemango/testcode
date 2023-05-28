from django.shortcuts import render,redirect
from .models import contact, news

def index(request):
    page = news.objects.all()
    return render(request, 'index.html', {"page":page})

def contactsave(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        new_contact = contact(name=name, email=email, subject=subject, meassage=message)
        print(new_contact,"aaa")
        new_contact.save()
    return render(request, 'contact.html', )
def contactlist(request):
    ct = contact.objects.all()
    print(ct, "aaaa")
    return render(request, 'new.html', {"ct":ct})

def uploaddata(request):
    if "submit1" in request.POST:
        print("kajal")
        category = request.POST.get('category')
        title = request.POST.get('title')
        details = request.POST.get('details')
        image = request.FILES.get('image')  
        
        obj = news(category=category, title=title, details=details, image=image)
        obj.save()
    upload = news.objects.all()
    return render(request, 'upload.html',{"upload": upload})

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