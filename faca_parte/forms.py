from django.forms import ModelForm, DateInput, Select, TextInput, Textarea
from django.utils.translation import ugettext_lazy as _

from models import Person


class PersonForm(ModelForm):

    class Meta:
        model = Person

        fields = ['select_role', 'schooling', 'full_name', 'email', 'birth', 'note', 'zipcode', 'street',
                  'street_complement', 'number', 'district', 'city', 'state', 'country']

        widgets = {
            'select_role': Select(attrs={'class': 'form-control', 'required': "",
                                         'data-error': _('Role must be included')}),
            'schooling': Select(attrs={'class': 'form-control'}),
            'full_name': TextInput(attrs={'class': 'form-control', 'autofocus': "true", 'required': "",
                                          'data-error': _('Name must be included')}),
            'email': TextInput(attrs={
                'class': 'form-control', 'type': 'email', 'data-error': _('Invalid email address'), 'required': "",
                'pattern': '^[_A-Za-z0-9-\+]+(\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\.[A-Za-z0-9]+)*(\.[A-Za-z]{2,})$'}),
            'birth': DateInput(attrs={'class': 'form-control datepicker'}),
            'zipcode': TextInput(attrs={'class': 'form-control', 'onBlur': 'pesquisacep(this.value);',
                                        'pattern': '\d{5}-?\d{3}',
                                        'placeholder': _('Enter your zip code that we will try to find your address')}),
            'street': TextInput(attrs={'class': 'form-control'}),
            # 'number': TextInput(attrs={'class': 'form-control'}),
            # 'street_complement': TextInput(attrs={'class': 'form-control'}),
            'district': TextInput(attrs={'class': 'form-control'}),
            'city': TextInput(attrs={'class': 'form-control'}),
            'state': TextInput(attrs={'class': 'form-control'}),
            # 'country': TextInput(attrs={'class': 'form-control'}),
            'note': Textarea(attrs={'class': 'form-control', 'rows': '4'}),
        }
