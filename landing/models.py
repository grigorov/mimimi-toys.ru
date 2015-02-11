from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Toys(models.Model):
    name = models.CharField(verbose_name="Имя игрушки:",max_length=256,help_text="Необходимо указать имя игрушки, максимальная длина имени 256 символов.")
    avatar = models.ImageField(upload_to='avatars',help_text="Большая картинка игрушки",verbose_name="Основное фото")
    avatar_thumbnail = ImageSpecField(source='avatar',processors=[ResizeToFill(200,180)],format='JPEG',options={'quality': 90})
    avatar_mini = ImageSpecField(source='avatar',processors=[ResizeToFill(180,143)],format='JPEG',options={'quality': 90})
    desc_mini = models.TextField(verbose_name="Описание игрушки кратко",help_text="Краткое описание игрушки, выводиться в ленте игрушек")
    desc_full = models.TextField(verbose_name="История игрушки",help_text="Полное описание игрушки, выводиться в подробном описании каждой игрушки")
    price = models.IntegerField(verbose_name="Стоимость игрушки",help_text="Необходимо указать стоимость игрушки в рублях",default=1000)
    avalable = models.BooleanField(verbose_name="В наличии",help_text="Указать, имеется ли в наличии",default=1)
    def admin_thumbnail(self):
        image = self.avatar
        if image:
            thumb = u'<img src="%s" />' % (self.avatar_mini.url)
        else:
            thumb = "No Image"
        return thumb
    admin_thumbnail.allow_tags = True

