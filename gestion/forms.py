from django.forms import ModelForm
from .models import Gestion
from django import forms

class AddGestionForm(ModelForm):
    class Meta:
        model = Gestion
        fields = ['name','cost_per_item','quantity_in_stock','quantity_sold']

class UpdateGestionForm(ModelForm):
    sales = forms.DecimalField(max_digits=19, decimal_places=2, disabled=True)

    class Meta:
        model = Gestion
        fields = ['name', 'cost_per_item', 'quantity_in_stock', 'quantity_sold']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['sales'] = self.instance.cost_per_item * self.instance.quantity_sold

