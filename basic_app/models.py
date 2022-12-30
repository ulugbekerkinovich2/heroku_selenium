from django.db import models


# Create your models here.

class Link(models.Model):
    link = models.CharField(max_length=500)
    path = models.FilePathField(path='C:/Users/ulugbek/Downloads/HISTORY OF MEDICINE (UZB)')
    upload = models.FileField(upload_to = user_directory_path)

    def __str__(self):
        return self.link

    class Meta:
        db_table = 'link'

# @receiver(post_save, sender=Link)
# def selenium_uploads(sender, instance, *args, **kwargs):
#     if instance.link:
#         selenium_upload1()
