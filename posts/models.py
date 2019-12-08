from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset()

class Dosya(models.Model):
    doc_name = models.CharField(max_length=150,verbose_name="Başlık")
    doc_content= models.TextField(max_length=10000,verbose_name="İçerik Hakkında")
    doc_image_link=models.CharField(max_length=1000,verbose_name="Görselin Adresi",
                                    help_text="Görselin yüklü bulunduğu esas link. 'örn:abc.com/resim.jpg | Resmin adresini kopyala'")
    doc_link=models.CharField(max_length=1000,verbose_name="Bağlantı Link",help_text="Yönlendirilecek Link",default="#")
    publishing_date=models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
    def __str__(self):
        return self.doc_name

    class Meta:
        ordering = ["-id"]

    def get_detail_url(self):
        return reverse('post:detail', kwargs={'id': self.id})

    def get_create_url(self):
        return reverse('post:create')

    def get_update_url(self):
        return reverse('post:update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('post:delete', kwargs={'id': self.id})