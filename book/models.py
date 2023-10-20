from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.CharField(max_length=20)
    isbn = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=15, decimal_places=2)  # decimal_places -> butun qismi qanchaligi
    language = models.CharField(max_length=15, blank=True, null=True)  # tili
    writing = models.CharField(max_length=15, blank=True, null=True)  # yozuv tili
    count_pages = models.IntegerField(blank=True, null=True)  # betlar soni
    publisher = models.CharField(max_length=40, blank=True, null=True)  # nashiryot
    cover = models.CharField(max_length=40, blank=True, null=True) # muqovasi
    paper_format = models.CharField(max_length=10, blank=True, null=True)  # qog'oz farmati
    year_of_publication = models.DateTimeField(auto_now_add=True)  # chop etilgan tili

    def __str__(self):
        return self.title