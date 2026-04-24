from django.shortcuts import render
from django.shortcuts import redirect
from .models import ContactMessage


from django.shortcuts import render, get_object_or_404
from .models import Service, Technology  # 1. Add Technology to your imports

def home(request):
    services = Service.objects.all()
    # 2. Fetch the technology data from the database
    technologies = Technology.objects.all() 
    
    # 3. Add 'technologies' to the context dictionary below
    return render(request, 'home.html', {
        'services': services, 
        'technologies': technologies
    })



def web_development(request):
    return render(request, 'web_development.html')


def graphic_design(request):
    return render (request,'graphic_design.html')


def app_development(request):
    return render (request,'app_development.html')


def seo(request):
    return render (request,'seo.html')



def uiux_design(request):
    return render (request,'uiux_design.html')



def contact_submit(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            service=request.POST.get("service"),
            message=request.POST.get("message"),
        )
    return redirect("home")