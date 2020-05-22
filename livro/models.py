from django.db import models

# Create your models here.
class Author(models.Model):

    name = models.CharField('Nome', max_length=250)

    def __str__(self):
        return self.name

class Book(models.Model):
    author  = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField('Título', max_length=250)
    pages = models.IntegerField('Número de Páginas')
    code = models.IntegerField('Código')

    def __str__(self):
        #return '%s - %s - %s - %s' %(self.author, self.title, self.code, self.pages)
        return self.title

