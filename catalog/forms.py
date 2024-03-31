from django import forms
from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         if field_name == 'is_current' or field_name == 'is_published':
    #             field.widget.attrs['class'] = 'form-check-input'
    #
    #         else:
    #             field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        # fields = ('name', 'description', 'price', 'image', 'category')
        exclude = ('created_at', 'updated_at')

    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for word in self.forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError("Данное название недопустимо.")
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for word in self.forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError("В описание товара было обнаружено недопустимое слово.")
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'