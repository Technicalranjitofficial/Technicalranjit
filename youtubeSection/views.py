import random

from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.


def YoutubeMain(request):
    object = list(YoutubeSection.objects.all())
    object_count=YoutubeSection.objects.all().count()
    othersVideo=random.sample(object,object_count)

    return render(request, "Youtubevideo/chechVideo.html", {'object': othersVideo})

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
    allpost = YoutubeSection.objects.all().order_by("created_date").reverse()
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
    return render(request, 'Youtubevideo/singlePost.html', context)



