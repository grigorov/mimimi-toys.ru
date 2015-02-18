from django import forms
from .models import Toys, Order


class OrderForm(forms.ModelForm):
    price = forms.IntegerField(widget=forms.HiddenInput)
    toy_id = forms.IntegerField(widget=forms.HiddenInput)
    email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    mob = forms.CharField(label="+79000000000",widget=forms.TextInput(attrs={'placeholder':'+79000000000','type':'tel'}),max_length=12)
    text = forms.CharField(label="Комментарий",widget=forms.Textarea(attrs={'cols':'5','rows':'5'}),max_length=200)
    def save(self):
        data = self.cleaned_data
        toy = Toys.objects.get(id=data['toy_id'])
        instance = Order(**data)
        instance.toy_id = toy.id
        instance.mob = data['mob']
        instance.price = data['price']
        instance.save()
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                if type(field.widget) in (forms.TextInput, ):
                    field.widget.attrs.update(
                        {'placeholder': field.label, 'class': 'span10'}
                    )
                if type(field.widget) in (forms.Select, ):
                    field.widget.attrs.update({'class': 'span10'})
                    field.empty_label = field.label

    def as_p(self):
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(field)s%(help_text)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True
        )

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Order
        exclude = ('done_is',)