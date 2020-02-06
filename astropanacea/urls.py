"""astropanacea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from homePage.views import loadHomePage
from blog.views import post_detail
from django.conf.urls.static import static
from django.conf import settings
from blogHome.views import loadAllPosts
from AboutUs.views import aboutUs
from QuoraHandler.views import loadAllQuora
from contactUsPage.views import loadContactUsPage,addUserQuery
from subscriberHandler.views import addSubscriber


# loadContactUsPage
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^markdownx/', include("markdownx.urls")),
    # url(r"^accounts/",include("registration.backends.hmac.urls")),
    url(
            regex='^(?P<post_id>\d+)/$',
            view=post_detail,
            name='post_detail',
        ),
    url(
            r"blogHome/",loadAllPosts,name="loadAllPosts"
        ),

    url(r'^about/', aboutUs, name="aboutUs"),
    url(r'^addSubscriber/', addSubscriber, name="addSubscriber"),
    url(r'^addUserQuery/',addUserQuery,name = "addUserQuery"),
    url(r'^quora/', loadAllQuora, name="loadAllQuora"),
    url(r'^contactUs/', loadContactUsPage, name="loadContactUsPage"),
    url(r'^home/', loadHomePage, name="loadHomePage"),
    url(r'^(?P<post_id>\d+)/comment/$', loadHomePage, name='loadHomePage'),
    url(r"^", loadHomePage, name="loadHomePage"),


]
if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
## https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
