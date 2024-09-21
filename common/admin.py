from django.contrib import admin

from .models import Media, Settings, Country, Region, OurInstagramStories, CustomerFeedback


admin.site.register(Media)
admin.site.register(Settings)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(OurInstagramStories)
admin.site.register(CustomerFeedback)
