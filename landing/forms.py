from django import forms
from .models import Toys, Order


class OrderForm(forms.ModelForm):
    name = forms.CharField(max_length=256, help_text="Укажите своё имя")
    price = forms.IntegerField(widget=forms.HiddenInput)
    toy_id = forms.IntegerField(widget=forms.HiddenInput)

    def save(self):
        data = self.cleaned_data
        toy = Toys.objects.get(id=data['toy_id'])
        Order.objects.create(name=data['name'],email=data['email'],mob=data['mob'],text=data['text'],price=int(data['price']), toy_id=toy.id)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Order
        exclude = ()