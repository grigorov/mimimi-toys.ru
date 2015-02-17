from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as OldFlatPageAdmin
from django.contrib.flatpages.admin import FlatpageForm as OldFlatpageForm
from redactor.widgets import RedactorEditor
from solo.admin import SingletonModelAdmin
from landing.models import SiteConfiguration, Toys, Gallery, Picture

class ToysAdmin(admin.ModelAdmin):
    list_display = ('name','admin_thumbnail','price')

admin.site.register(Toys, ToysAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title',)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Gallery,GalleryAdmin)
admin.site.register(Picture,PictureAdmin)

class FlatpageForm(OldFlatpageForm):
    #content = forms.CharField(widget=RedactorEditor())
    class Meta:
        model = FlatPage
        exclude = ()
        widgets = {
           'content': RedactorEditor(),
        }

class FlatPageAdmin(OldFlatPageAdmin):
    form = FlatpageForm

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(SiteConfiguration, SingletonModelAdmin)
