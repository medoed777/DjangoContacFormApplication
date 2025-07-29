from django.forms import ModelForm
from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ("created_at", "updated_at",)

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
            self.add_error("price", f"Цена не может быть меньше 0")
        return price

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        word_valid = [
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

        if name:
            if any(word in name for word in word_valid):
                self.add_error("name", f'Название не может содержать недопустимые слова: {", ".join(word_valid)}')

        if description:
            if any(word in description for word in word_valid):
                self.add_error("description",
                               f'Описание не может содержать недопустимые слова: {", ".join(word_valid)}')