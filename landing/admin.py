from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as OldFlatPageAdmin
from django.contrib.flatpages.admin import FlatpageForm as OldFlatpageForm
from redactor.widgets import RedactorEditor
from solo.admin import SingletonModelAdmin
from landing.models import SiteConfiguration, Toys

# Register your models here.

class ToysAdmin(admin.ModelAdmin):
    list_display = ('name','admin_thumbnail','price')
admin.site.register(Toys,ToysAdmin)

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
