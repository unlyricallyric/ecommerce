from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .models import BlogPost



def blog_post_detail_page(request, slug):

    # try:
    queryset = BlogPost.objects.filter(slug = slug)
    obj = queryset.first()
    #obj = get_object_or_404(BlogPost, slug=slug)

    template_name = 'blog_post_detail_page.html'
    context = {"object": obj}
    return render(request, template_name, context)

#for several objects
def blog_post_list_view(request):
    #list out objects or search objects
    qs = BlogPost.objects.all()
    #qs = BlogPost.objects.filter(title_icontains='sometext')
    template_name = 'blog_post_list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)

def blog_post_create_view(request):
    #create objects
    #use form
    template_name = 'blog_post_create.html'
    context = {'object_form': None}
    return render(request, template_name, context)

#for 1 single object
def blog_post_detail_view(request):
    #one object or the detail view
    obj = get_object_or_404(BlogPost, slug = slug)
    template_name = 'blog_post_detail.html'
    context = {'object_': obj}
    return render(request, template_name, context)

def blog_post_update_view(request):
    template_name = 'blog_post_update.html'
    context = {'object': obj, 'form': None}
    return render(request, template_name, context)

def blog_post_delete_view(request):
    template_name = 'blog_post_delete.html'
    context = {'object': obj}
    return render(request, template_name, context)
