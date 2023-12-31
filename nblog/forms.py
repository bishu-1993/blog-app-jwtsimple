from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','body','header_image')

        widgets = {
            'title':forms.TextInput(attrs={'class' :'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'eld', 'type':'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            # 'header_image': forms.ClearableFileInput(attrs={'class': 'form-control'})

        }

    header_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'custom-file-input'}),
                                    required=False)