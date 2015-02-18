from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from solo.models import SingletonModel
from phonenumber_field.modelfields import PhoneNumberField

class Picture(models.Model):
    title = models.CharField(max_length=50,verbose_name="Имя картинки",help_text="укажите имя картинки")
    image = models.ImageField(upload_to='gallery',verbose_name="Изображение",help_text="укажите изображение")
    image_mini = ImageSpecField(source='image',processors=[ResizeToFill(380,380)],format='JPEG')
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Изображение для галлереи"
        verbose_name_plural = "Изображения для галлереи"

class Gallery(models.Model):
    title = models.CharField(max_length=50)
    pictures = models.ManyToManyField(Picture)
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Галлерея"
        verbose_name_plural = "Галлереи"



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
    avatar_thumbnail = ImageSpecField(source='avatar',processors=[ResizeToFill(380,380)],format='JPEG',options={'quality': 90})
    avatar_mini = ImageSpecField(source='avatar',processors=[ResizeToFill(160,160)],format='JPEG',options={'quality': 90})
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
        ordering = ('id',)

    def admin_thumbnail(self):
        image = self.avatar
        if image:
            thumb = u'<img src="%s" />' % (self.avatar_mini.url)
        else:
            thumb = "No Image"
        return thumb
    admin_thumbnail.allow_tags = True

class Order(models.Model):
    DONE_CHOICES = (
        ('Done','Выполнен'),
        ('Undone','Не Выполнен'),
    )
    name = models.CharField(max_length=255,verbose_name="Имя",help_text="Укажите имя, это поле обязательное. ")
    email = models.EmailField(verbose_name="Email",help_text="Поле обязательно для заполнения")
    mob = PhoneNumberField(verbose_name="Ваш номе телефона",help_text="Укажите номер телефона, это поле обязательно для заполнения, максимальное кол-во цифр 12, пример: +74957777777",max_length=12)
    text = models.TextField(verbose_name="Комментарий к заказу",help_text="Укажите комментарий к заказу",null=True,blank=True,default="Станция метро:")
    price = models.IntegerField(verbose_name="Цена",null=True,blank=True)
    toy_id = models.IntegerField(verbose_name="Игрушка",null=True,blank=True)
    done_is = models.CharField(choices=DONE_CHOICES,verbose_name="Выполнен ли заказ?",default='Undone',max_length=6)

    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"