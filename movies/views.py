from django.shortcuts import render,get_object_or_404,redirect
from.models import Movie,Rating
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Movie,Rating,Review,Watchlist


@login_required(login_url="/Login/")
def movie_list(request):
    search = request.GET.get("search")
    category = request.GET.get("category")

    movies = Movie.objects.all()

    # 🔍 search filter
    if search:
        movies = movies.filter(title__icontains=search)

    # 🎭 category filter
    if category:
        movies = movies.filter(category__iexact=category)

    return render(request, "movies/movie_list.html", {"movies": movies})



@login_required(login_url="/Login/")
def Movie_detail(request,id):
    movie=get_object_or_404(Movie,id=id)
    return render(request,"movies/movie_detail.html",{"movie":movie})

def Home(request):
    return render(request,"movies/home.html")


def signup_view(request):
    error = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            error = "Username already exists"
        else:
            user = User.objects.create_user(
                username=username,
                password=password
            )
            login(request, user)
            return redirect("/movie_list/")

    return render(request, "movies/signup.html", {"error": error})



def login_view(request):
    error = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/movie_list/")
        else:
            error = "Invalid username or password"

    return render(request, "movies/movie_list.html", {"error": error})

def logout_view(request):
    logout(request)
    return redirect("/Login/")

def Add_rating(request,id):
     if request.method == "POST":
        movie = get_object_or_404(Movie, id=id)
        stars = request.POST.get("stars")


        if stars is not None:
            stars=int(stars)

        # create or update rating (1 user → 1 rating)
        Rating.objects.update_or_create(
            movie=movie,
            user=request.user,
            defaults={"stars": stars}
        )

     return redirect(f"/movie/{id}/")


@login_required
def Add_review(request,id):
    if request.method=="POST":
        movie=Movie.objects.get(id=id)
        comment=request.POST.get("comment")


        Review.objects.create(
            movie=movie,
            user=request.user,
            comment=comment
        )

    return redirect(f"/movie/{id}/")

@login_required
def add_watchlist(request,id):
    movie=get_object_or_404(Movie,id=id)

    Watchlist.objects.get_or_create(
        user=request.user,
        movie=movie
    )
    return redirect("/movie/"+str(id)+"/")

@login_required
def remove_watchlist(request,id):
    movie=get_object_or_404(Movie,id=id)
    Watchlist.objects.filter(
        user=request.user,
        movie=movie
    ).delete()

    return redirect("/movie/"+str(id)+"/")

@login_required
def my_watchlist(request):
    movies=Watchlist.objects.filter(user=request.user)
    return render(request,"movies/watchlist.html",{"movies":movies})

@login_required
def Watchlist_view(request):
   movies=Watchlist.objects.filter(user=request.user)
   return render(request,"movies/watchlist.html",{"movies":movies})

    

