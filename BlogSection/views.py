from django.shortcuts import render, get_object_or_404
from .models import *

def blogMainPage(request):
    post=BlogSection.objects.all().order_by('created_date').reverse()
    return render(request,'blog_main_page.html',{'post':post})

def single_post(request):
    return render(request,'blog_single_page.html')


def BlogSingle(request, slug, pk):
    post = get_object_or_404(BlogSection, pk=pk, slug=slug, )
    allpost = BlogSection.objects.all().order_by("created_date").reverse()
    # reviews = Software_Review.objects.filter(soft_post=post)
    # if request.method == 'POST':
    #     review = SoftwareReviewForm(request.POST or None)
    #     if review.is_valid():
    #         rv = request.POST.get('review')
    #         save = Software_Review.objects.create(soft_post=post, posted_user=request.user, review=rv)
    #         save.save()
    #         return HttpResponseRedirect(request.path_info)
    # else:
    #     review = SoftwareReviewForm()
    # 'review': review,

    context = {'post': post,'allpost': allpost,}
    return render(request, 'blog_single_page.html', context)


def blog_all_post(request):
    post = BlogSection.objects.all().order_by('created_date').reverse()
    return render(request,'blog_all_post.html',{'post':post})
