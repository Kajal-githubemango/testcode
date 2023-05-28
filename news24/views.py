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
    martial_status = [
        ('Tech', 'Tech'),
        ('Sports', 'Sports'),
        ('Fashion', 'Fashion'),
    ]
    if request.method == 'POST':
        category = request.POST.get('category')
        title = request.POST.get('title')
        details = request.POST.get('details')
        image = request.FILES.get('images')  
        
        obj = news(category=category, title=title, details=details, image=image)
        obj.save()
        # categories = list(news.objects.all().values_list('category',flat=True))
        # print(categories, "sdddd")
    return render(request, 'upload.html', {'martial_status': martial_status})
