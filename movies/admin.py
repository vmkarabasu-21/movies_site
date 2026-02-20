from django.contrib import admin
from .models import Movie
from .models import Review

@admin.register(Movie)
class Moviesadmin(admin.ModelAdmin):
    list_display=("title","year","avg_rating")

    def avg_rating(self,obj):
        return obj.average_rating()
    
    avg_rating.short_description="⭐ Avg Rating"

admin.site.register(Review)
