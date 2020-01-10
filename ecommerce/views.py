from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
    title = "I'm a new title"
    context = {"title": title, "user_data": [1,2,3,4]}
    return render(request, "home.html", context)

def about_page(request):
    return render(request, "about.html", {"title":"About Us"})

def contact_page(request):
    return render(request, "contact.html", {"title": "Contact us"})

def example(request):
    context = {"title": "Example Page"}
    template_name = "hello_world.html"
    #template_obj = get_template(template_name)
    return HttpResponse(get_template(template_name).render(context))


