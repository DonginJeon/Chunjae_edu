"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


# URL을 보내는 곳
urlpatterns = [
    path("admin/", admin.site.urls),
]
    # catalog > urls.py를 바라본다
urlpatterns += [
    path('catalog/', include('catalog.urls')),
    path("", RedirectView.as_view(url='/catalog/', permanent=True))
]

# 자바 스크립트를 사용하는 곳
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# 인증용 URL 만들기
urlpatterns += [
    path("accounts/",include("django.contrib.auth.urls"))
]