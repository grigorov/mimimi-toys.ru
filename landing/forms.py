from django import forms
from .models import Toys, Order


class OrderForm(forms.ModelForm):
    price = forms.IntegerField(widget=forms.HiddenInput)
    toy_id = forms.IntegerField(widget=forms.HiddenInput)
    mob = forms.CharField(label="Моб/Телефон",widget=forms.TextInput(attrs={'type':'tel'}),max_length=12,help_text="Укажите номер телефона. Наш менеджер с вами свяжиться.")
    text = forms.CharField(label="Комментарий",widget=forms.Textarea(attrs={'cols':'5','rows':'5'}),max_length=200,help_text="Укажите комментарий к заказу, станция метро где удобно было бы забрать, время в которое удобно было бы вам.")
    def save(self):
        data = self.cleaned_data
        toy = Toys.objects.get(id=data['toy_id'])
        instance = Order(**data)
        instance.toy_id = toy.id
        instance.save()

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Order
        exclude = ('done_is',)