from django.contrib import admin
from apps.library.models import Genre, Author, Book, Rating


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)
    list_filter = ('created_at',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'birth_date', 'death_date')
    search_fields = ('first_name', 'last_name')
    list_filter = ('birth_date', 'death_date')
    ordering = ('last_name', 'first_name')


class RatingInline(admin.TabularInline):
    model = Rating
    extra = 0
    readonly_fields = ('user', 'rating')
    can_delete = False


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'author', 'genre', 'published_date',
        'price', 'discount', 'copies_sold'
    )
    search_fields = ('title', 'description', 'author__first_name', 'author__last_name')
    list_filter = ('genre', 'author', 'published_date')
    ordering = ('-published_date',)
    inlines = [RatingInline]


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'rating', 'created_at')
    search_fields = ('user__username', 'book__title')
    list_filter = ('rating', 'created_at')
    ordering = ('-created_at',)
