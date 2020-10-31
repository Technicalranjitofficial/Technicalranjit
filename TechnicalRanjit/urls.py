"""TechnicalRanjit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
