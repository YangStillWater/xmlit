from django.db import models

class Image(models.Model):
    def __str__(self):
        return self.filename

    position = models.CharField(max_length=200)
    filename = models.CharField(max_length=200)
    upd_person = models.CharField(max_length=200)
    upd_date = models.DateTimeField('date published')

class SlideImage(models.Model):
    def __str__(self):
        return self.filename

    filename = models.CharField(max_length=200)
    upd_person = models.CharField(max_length=200)
    upd_date = models.DateTimeField('date published')

class Text(models.Model):
    def __str__(self):
        return self.content

    position = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    upd_person = models.CharField(max_length=200)
    upd_date = models.DateTimeField('date published')
