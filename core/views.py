from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from .forms import PhotoForm, CommentForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.conf import settings
import base64
import uuid
from django.core.files.base import ContentFile

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()
            return redirect('view_links', photo_id=photo.id)
    else:
        form = PhotoForm()
    return render(request, 'upload.html', {'form': form})

def view_links(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    return render(request, 'links.html', {'photo': photo})

def view_comments(request, photo_id, token):
    photo = get_object_or_404(Photo, id=photo_id, secret_token=token)
    comments = photo.comments.all()
    return render(request, 'comments.html', {'photo': photo, 'comments': comments})

def photo_page(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.photo = photo

            # 📌 Gestion de l'audio Base64
            audio_base64 = request.POST.get('audio', None)
            if audio_base64:
                format, audio_str = audio_base64.split(';base64,')
                ext = format.split('/')[-1]
                audio_file = ContentFile(base64.b64decode(audio_str), name=f'{uuid.uuid4()}.{ext}')
                comment.audio = audio_file

            comment.save()

            # 📧 Génération du lien pour voir tous les commentaires
            comment_url = request.build_absolute_uri(
                reverse('view_comments', args=[photo.id, photo.secret_token])
            )

            # 🔥 Rendu du contenu HTML pour l’email
            html_content = render_to_string("email_template.html", {
                'comment_content': comment.content,
                'comment_url': comment_url
            })

            # 📨 Contenu texte fallback
            text_content = f"""
Tu as reçu un nouveau commentaire :

"{comment.content}"

Voir tous les commentaires : {comment_url}
""".strip()

            # 💌 Envoi de l’email
            email = EmailMultiAlternatives(
                subject="📨 Nouveau commentaire anonyme reçu",
                body=text_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[photo.email],
            )
            email.attach_alternative(html_content, "text/html")
            email.send()

            return redirect(f"{request.path}?sent=1")
    else:
        form = CommentForm()

    return render(request, 'photo.html', {'photo': photo, 'form': form})

def robots_txt(request):
    return render(request, 'robots.txt', {'domain': request.get_host()}, content_type='text/plain')
