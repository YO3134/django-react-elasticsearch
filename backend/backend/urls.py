"""backend URL Configuration

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
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from book import views

# routersはrailsライクな自動URLルーティング機能を提供する
router = routers.DefaultRouter()
router.register(r"book", views.BookView, "book")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls))
    # path("booksearch/", include("booksearch.urls")),
    # path("", RedirectView.as_view(url="booksearch/")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# 開発時の静的ファイルurl生成
