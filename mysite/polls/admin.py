from django.contrib import admin
from polls.models import Poll, Choice

# Register your models here.
class ChioceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields' : ['question']}),
        ('Date information',{'fields' : ['pub_date'], 'classes' : ['collapse']}),
    ]
    inlines = [ChioceInline]

admin.site.register(Poll,PollAdmin)
