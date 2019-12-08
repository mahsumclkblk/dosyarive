from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect
from posts.models import Dosya
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home_page(request):
    posts=Dosya.objects.all()
    paginator = Paginator(posts, 8)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)


    context={
        "posts":posts,
    }
    return render(request,"home_templates/home_page.html",context)