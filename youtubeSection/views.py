import random

from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.


def YoutubeMain(request):
    recent_post=YoutubeSection.objects.all().order_by("created_date").reverse()
    object = list(YoutubeSection.objects.all())
    object_count=YoutubeSection.objects.all().count()
    othersVideo=random.sample(object,object_count)

    return render(request, "Youtubevideo/chechVideo.html", {'object': othersVideo,'recent_post':recent_post})

    # query = request.GET.get('q')
    # if query:
    #     obj = YoutubeSection.objects.filter(
    #         Q(software_name__icontains=query) |
    #         Q(overview__icontains=query) |
    #         Q(overview_desc1__icontains=query) |
    #         Q(overview_desc2__icontains=query) |
    #         Q(features__icontains=query) |
    #         Q(features_desc__icontains=query)
    #
    #     )
    #     html = "Result found with"
    #     messages.success(request, html)



def ViseoSingle(request, slug, pk):
    post = get_object_or_404(YoutubeSection, pk=pk, slug=slug, )
    recent_post=YoutubeSection.objects.all().order_by("created_date").reverse()
    allpost = list(YoutubeSection.objects.all())
    object_counts = YoutubeSection.objects.all().count()
    othersVideo = random.sample(allpost,object_counts )

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

    context = {'post': post,'allpost': othersVideo,"recent_post":recent_post}
    return render(request, 'Youtubevideo/singlePost.html', context)


def search_result(request):

    obj = YoutubeSection.objects.all().order_by("created_date")
    query = request.GET.get('q')
    if query:
        obj = YoutubeSection.objects.filter(
            Q(title__contains=query) |
            Q(description__icontains=query)
        )
        html = "Result found with"
        messages.success(request, html)

    return render(request,'Youtubevideo/search_result.html',{"object":obj})



