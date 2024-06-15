from django.contrib import admin
from . models import BookStore, IssueBook, Program, Branch, Year
# Register your models here.
admin.site.register(BookStore)
admin.site.register(IssueBook)
admin.site.register(Program)
admin.site.register(Branch)
admin.site.register(Year)


