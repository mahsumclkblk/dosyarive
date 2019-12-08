from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect
from posts.models import Dosya
from .forms import DosyaForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from taggit.models import Tag
from django.db.models import Count
from django.contrib.auth.decorators import login_required




def post_index(request):

    post_list=Dosya.objects.all()
    last_post=Dosya.objects.first()
    tag_list=Dosya.tags.all()
    query=request.GET.get("q")
    query_for_tag=request.GET.get("tag")


    #Searching

    if query:
        post_list=post_list.filter(
            Q(doc_name__icontains=query)|
            Q(doc_content__icontains=query) |
            Q(doc_link__icontains=query)
        ).distinct()

    if query_for_tag:
        post_list=post_list.filter(
            Q(tags__name=query_for_tag)
        )
    #TAGGING_SEARCHING

    # if query_for_tag:
    #     post_list=post_list.filter(
    #         Q(tags__icontains=query_for_tag)
    #     ).distinct()


    # Q(user__first_name__icontains=query) |
    # Q(user__last_name__icontains=query))

    #pagination

    paginator = Paginator(post_list,8)# Show 25 contacts per page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)


    #TAGS
    paginator = Paginator(tag_list,12)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        tag_list = paginator.page(page)
    except PageNotAnInteger:
        tag_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        tag_list = paginator.page(paginator.num_pages)
    context = {"posts": posts,
               "last_post": last_post,
               "tags": tag_list}



    return render(request,"post_template/index.html",context)



@login_required(login_url="/post/index/")
def post_create(request):
    forms=DosyaForm(request.POST or None)
    if forms.is_valid():
        post=forms.save()
        return HttpResponseRedirect(post.get_detail_url())

    return render(request,"post_template/form_create.html",context={"forms":forms})

def post_detail(request,id):
    post=get_object_or_404(Dosya,id=id)
    last_post=Dosya.objects.first()
    post_list=Dosya.objects.all()

    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = post_list.filter(tags__in=post_tags_ids).exclude(id=id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags')[:4]

    return render(request,"post_template/post_detail.html",{"post":post,"last_post":last_post,'similar_posts': similar_posts})

@login_required(login_url="/post/index/")
def post_update(request,id):
    post=get_object_or_404(Dosya,id=id)
    forms=DosyaForm(request.POST or None,instance=post)
    if forms.is_valid():
        forms.save()
        return HttpResponseRedirect(post.get_detail_url())


    return render(request,"post_template/form_update.html",context={"forms":forms,"post":post})

@login_required(login_url="/post/index/")
def post_delete(request,id):
    post=get_object_or_404(Dosya,id=id)
    post.delete()

    return redirect("post:index")


