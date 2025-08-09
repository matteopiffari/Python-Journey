# Every time you create a new model, remember to register it in admin.py
# Then run `python manage.py makemigrations` and `python manage.py migrate` to apply the changes.


from django.db import models

# Create your models here.

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    