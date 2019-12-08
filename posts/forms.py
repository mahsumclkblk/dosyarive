from django import forms
from .models import Dosya

class DosyaForm(forms.ModelForm):
    class Meta:
        model= Dosya
        fields='__all__'

#
# class PostForm(forms.Form):
#     doc_name = forms.CharField(label="Başlık",widget=forms.TextInput(attrs={'placeholder': 'Dosyayı tanımlayacak bir başlık'}))
#     doc_content = forms.CharField(label="İçerik",
#         widget=forms.Textarea(attrs={'placeholder': 'İligili içeriği tanımlayın.'})
#     )
#
#     doc_image_link = forms.CharField(label="Görsel Linki",
#         widget=forms.TextInput(attrs={'placeholder': 'örn: herhangibirlink.jpg'})
#     )
#     doc_link = forms.CharField(label="Adres",
#         widget=forms.TextInput(attrs={'placeholder': 'örn :burayagidecek.com'})
#     )
