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
    def clean(self):
        cleaned_data = super().clean()
        image = cleaned_data.get("image")
        video = cleaned_data.get("video")

        if not image and not video:
            raise forms.ValidationError("Vous devez uploader soit une image, soit une vidéo.")
        if image and video:
            raise forms.ValidationError("Vous ne pouvez pas uploader une image et une vidéo en même temps.")
        return cleaned_data

class CommentForm(forms.ModelForm):
    class Meta:
        model = AnonymousComment
        fields = ['content', 'audio']  # ajout du champ audio

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Ton commentaire anonyme...'
        })
        self.fields['audio'].widget.attrs.update({
            'class': 'form-control',
            'accept': 'audio/*'
        })
