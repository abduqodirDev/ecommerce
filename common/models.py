from django.db import models


class Media(models.Model):
    class FileType(models.TextChoices):
        IMAGE = 'image', 'image'
        FILE = 'file', 'file'
        MUSIC = 'music', 'music'
        VIDEO = 'video', 'video'

    file = models.FileField(upload_to='files/')
    type = models.CharField(max_length=10, choices=FileType.choices)

    def __str__(self):
        return self.id


class Settings(models.Model):
    image = models.ForeignKey(Media, on_delete=models.SET_NULL, blank=True, null=True)
    home_title = models.CharField(max_length=30)
    home_subtitle = models.CharField(max_length=100)

    def __str__(self):
        return self.home_title


class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, related_name='regions', null=True, blank=True)

    def __str__(self):
        return self.name


class OurInstagramStories(models.Model):
    image = models.ForeignKey(Media, on_delete=models.SET_NULL, related_name='instagram_stores', null=True, blank=True)
    story_link = models.URLField()      # write validatsiya

    def __str__(self):
        return self.id


class CustomerFeedback(models.Model):
    description = models.TextField()
    rank = models.IntegerField()
    customer_name = models.CharField(max_length=100)
    customer_position = models.CharField(max_length=100)
    customer_image = models.ForeignKey(Media, on_delete=models.SET_NULL, related_name='custom_feedbacks', null=True, blank=True)

    def __str__(self):
        return self.customer_name
