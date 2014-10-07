from django.db import models

class FontEntry(models.Model):
    font_name = models.CharField(max_length=30)
    font_url = models.CharField(max_length=300)

    def __str__(self):
        return self.font_name

class ChosenFont(models.Model):
    font_class = models.CharField(max_length=30)
    font_entry = models.ForeignKey('FontEntry')
    color = models.CharField(max_length=6) 
    size = models.IntegerField() 

    def __str__(self):
        return self.font_entry.font_name
 
