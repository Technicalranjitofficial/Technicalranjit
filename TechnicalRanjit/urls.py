
from django.contrib import admin
from django.urls import path
from Tr.views import *
from django.conf import settings
from django.conf.urls.static import static
from youtubeSection.views import *
from BlogSection.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    # video section
    path('VideoSection/',YoutubeMain,name="youtube_section"),
    path('VideoSection/<int:pk>/<slug:slug>', ViseoSingle, name="singleVideo"),
    # blog section
    path('blog_main/',blogMainPage,name="blog_main"),
    path('blog_main/allpost',blog_all_post,name="blog_allpost"),
    path('blogPost/<int:pk>/<slug:slug>',BlogSingle,name="blog_single_post"),

#     policy related

    path('privacy-policy/',privacypolicy,name="privacy_policy"),
    path('terms_conditions/', termscondition, name="terms_conditions"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
