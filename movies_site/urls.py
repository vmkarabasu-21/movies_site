"""
URL configuration for movies_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from movies.views import movie_list,Movie_detail,Home,login_view,signup_view,logout_view,Add_rating,Add_review
from movies.views import add_watchlist,remove_watchlist,Watchlist_view
urlpatterns = [
    path("",Home,name="HOME"),
    path('admin/', admin.site.urls),
    path("movie_list/",movie_list,name="movies"),
    path("movie/<int:id>/",Movie_detail,name="Movie_details"),
    path("Login/",login_view,name="login"),
    path("signup/",signup_view,name="signup"),
    path("logout/",logout_view,name="logout"),
    path("rate/<int:id>/",Add_rating),
    path("review/<int:id>/",Add_review,name="add_review"),
    path("watchlist/add/<int:id>/",add_watchlist,name="add_watchlist"),
    path("watchlist/remove/<int:id>/",remove_watchlist,name="remove_watchlist"),
    path("Watchlist/",Watchlist_view,name="Watchlist")


]   

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
