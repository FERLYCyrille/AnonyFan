from django import forms
from .models import Photo, AnonymousComment

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'video', 'email']  # ajout du champ video

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['video'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ton email (requis pour recevoir les messages)'
        })
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = AnonymousComment
        fields = ['content']  # ajout du champ audio

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Ton commentaire anonyme...'
        })
        