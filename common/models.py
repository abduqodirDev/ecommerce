from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import FileExtensionValidator

from common.validators import UrlCheckValidator


class Media(models.Model):
    class FileType(models.TextChoices):
        IMAGE = 'image', 'image'
        FILE = 'file', 'file'
        MUSIC = 'music', 'music'
        VIDEO = 'video', 'video'

    file = models.FileField(upload_to='files/', validators=[
        FileExtensionValidator(allowed_extensions=['.png', '.jpg', 'jpeg', 'gif', 'mp4', 'mp3', 'wav', 'flac', '.doc', '.pdf'])])
    type = models.CharField(max_length=10, choices=FileType.choices)

    def __str__(self):
        return str(self.id)

    def clean(self):
        if self.type == Media.FileType.IMAGE:
            if not self.file.name.endswitch(['.png', '.jpg', '.jpeg', '.gif']):
                raise ValidationError("file type is not image")
        elif self.type == Media.FileType.FILE:
            if not self.file.name.endswitch(['.doc', '.pdf']):
                raise ValidationError("file type is not file")
        elif self.type == Media.FileType.MUSIC:
            if not self.file.name.endswitch(['.mp3', '.flac']):
                raise ValidationError("file type is not music")
        elif self.type == Media.FileType.VIDEO:
            if not self.file.name.endswitch(['.mp4']):
                raise ValidationError("file type is not video")
        else:
            raise ValidationError("File type is invalid")


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
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, related_name='regions', null=True, blank=True)

    def __str__(self):
        return self.name


class OurInstagramStories(models.Model):
    image = models.ForeignKey(Media, on_delete=models.SET_NULL, related_name='instagram_stores', null=True, blank=True)
    story_link = models.URLField(validators=[UrlCheckValidator])

    def __str__(self):
        return str(self.story_link)


class CustomerFeedback(models.Model):
    description = models.TextField()
    rank = models.IntegerField()
    customer_name = models.CharField(max_length=100)
    customer_position = models.CharField(max_length=100)
    customer_image = models.ForeignKey(Media, on_delete=models.SET_NULL, related_name='custom_feedbacks', null=True, blank=True)

    def __str__(self):
        return self.customer_name
