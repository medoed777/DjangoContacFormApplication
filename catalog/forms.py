from django.core.exceptions import ValidationError
from django.forms import ModelForm
from catalog.models import Product


WORD_VALID = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = (
            "created_at",
            "updated_at",
            "owner",
        )

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите наименование товара"}
        )

        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание"}
        )

        self.fields["category"].widget.attrs.update(
            {
                "class": "form-select",
            }
        )

        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "type": "number"}
        )

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price and price < 0:
            raise ValidationError(f"Цена не может быть меньше 0")
        return price

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        if name:
            if any(word in name for word in WORD_VALID):
                self.add_error(
                    "name",
                    f'Название не может содержать недопустимые слова: {", ".join(WORD_VALID)}',
                )

        if description:
            if any(word in description for word in WORD_VALID):
                self.add_error(
                    "description",
                    f'Описание не может содержать недопустимые слова: {", ".join(WORD_VALID)}',
                )


class ProductModeratorForm(ModelForm):
    class Meta:
        model = Product
        fields = ("status",)
