from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from solo.models import SingletonModel

class Picture(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='gallery')
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title

class Gallery(models.Model):
    title = models.CharField(max_length=50)
    pictures = models.ManyToManyField(Picture)
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title

class SiteConfiguration(SingletonModel):
    name = models.CharField(max_length=255, default='Mimimi Toys',verbose_name="Название сайта",help_text="Например: Mimimi Toys")
    title = models.CharField(max_length=255, default="Mimimi-toys.ru - Магазин уникальных игрушек",verbose_name="Заголовк страницы",help_text="Заголовок отображается в заголовках страницы браузера")
    slogan = models.CharField(max_length=255,default="Магазин уникальных игрушек ручной работы",verbose_name="Слоган",help_text="Слоган который отображется на главной странице под названием сайта.")
    slider_header = models.CharField(max_length=255,default="<strong>Mimimi Toys -</strong> Игрушки с душой",verbose_name="Заголовк слайдера")
    vk_url = models.URLField(verbose_name="Ссылка в Вконтакте",help_text="ССылка на группу или страницу Вконтакте",default="http://vk.com")
    fb_url = models.URLField(verbose_name="Ссылка в Facebook",help_text="Ссылка на группу или страницу в Facebook",default="http://facebook.com")
    instagram_url = models.URLField(verbose_name="Ссылка в Instagam",help_text="ссылка на страницу в Instagram",default="http://instagram.com")

    def __unicode__(self):
        return "Конфигурация сайта"

    class Meta:
        verbose_name = "Конфигурация сайта"

# Create your models here.
class Toys(models.Model):
    name = models.CharField(verbose_name="Имя игрушки:",max_length=256,help_text="Необходимо указать имя игрушки, максимальная длина имени 256 символов.")
    avatar = models.ImageField(upload_to='avatars',help_text="Большая картинка игрушки",verbose_name="Основное фото")
    avatar_thumbnail = ImageSpecField(source='avatar',processors=[ResizeToFill(200,180)],format='JPEG',options={'quality': 90})
    avatar_mini = ImageSpecField(source='avatar',processors=[ResizeToFill(180,143)],format='JPEG',options={'quality': 90})
    desc_mini = models.TextField(verbose_name="Описание игрушки кратко",help_text="Краткое описание игрушки, выводиться в ленте игрушек")
    desc_full = models.TextField(verbose_name="История игрушки",help_text="Полное описание игрушки, выводиться в подробном описании каждой игрушки")
    price = models.IntegerField(verbose_name="Стоимость игрушки",help_text="Необходимо указать стоимость игрушки в рублях", default=1000)
    avalable = models.BooleanField(verbose_name="В наличии",help_text="Указать, имеется ли в наличии", default=1)
    image_gallery = models.ForeignKey(Gallery,null=True,blank=True)

    def __unicode__(self):
        return "Игрушки"

    class Meta:
        verbose_name = "Игрушки"
        verbose_name_plural = "Игрушки"

    def admin_thumbnail(self):
        image = self.avatar
        if image:
            thumb = u'<img src="%s" />' % (self.avatar_mini.url)
        else:
            thumb = "No Image"
        return thumb
    admin_thumbnail.allow_tags = True

