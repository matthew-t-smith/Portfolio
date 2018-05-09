from django.db import models
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=20)
    platform = models.CharField(max_length=20, null=True)
    link = models.URLField(null=True)
    readme = models.FileField(upload_to='readmes', storage=gd_storage, null=True)
    stack = models.TextField()
    date = models.DateField(default="2018-05-07")

    def __str__(self):
        return f"{self.name}"

class Image(models.Model):
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=20)
    img = models.ImageField(upload_to='images', storage=gd_storage)
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.name} for {self.project}"
