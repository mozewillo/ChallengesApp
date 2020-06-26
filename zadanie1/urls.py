"""zadanie1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from challenges import views

urlpatterns = [
    # website
    url(r'^$', views.showChallenges),
    url(r'^admin/', admin.site.urls),

    # ajax
    url(r'^ajax/increment/', views.ajaxIncrement),
    url(r'^ajax/save/', views.ajaxSaveChallenge),
    url(r'^ajax/delete', views.ajaxDeleteChallenge),
    url(r'^ajax/getchallenge/', views.ajaxGetChallenge),
]
