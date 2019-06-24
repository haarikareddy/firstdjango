from django.contrib import admin
from home.models import Book
from home.models import Genre,Author,Customer
# Register your models here.

#admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Customer)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields=('id','name')
    #note : RelatedOnlyField => applicable when some fields are related to other tables
    list_filters=('name','purchase_date',('author',admin.RelatedOnlyFieldListFilter))
    list_filter=('name','purchase_date','author')
