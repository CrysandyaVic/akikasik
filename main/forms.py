from django.forms import ModelForm
from main.models import Products
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ["nama", "harga", "deskripsi"]
    
    def clean_mood(self):
        nama = self.cleaned_data["nama"]
        return strip_tags(nama)

    def clean_feelings(self):
        deskripsi = self.cleaned_data["deskripsi"]
        return strip_tags(deskripsi)