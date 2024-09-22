from django.contrib import admin

from .models import Media, Settings, Country, Region, OurInstagramStories, CustomerFeedback


admin.site.register(Media)
admin.site.register(Settings)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(OurInstagramStories)

class CustomerFeedbackAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

admin.site.register(CustomerFeedback, CustomerFeedbackAdmin)
