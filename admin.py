from django.contrib import admin
from models import Storyline

class StorylineAdmin(admin.ModelAdmin):
    list_display = ('title','total','first','last')
    prepopulated_fields = {'slug': ('title',),}
    
    def total(self, obj):
        """
        Returns number of comics associated with storyline
        """
        return obj.comics.all().count()


admin.site.register(Storyline,StorylineAdmin)