from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Photo, AnonymousComment

class AnonymousCommentInline(admin.TabularInline):
    model = AnonymousComment
    extra = 1
    readonly_fields = ('created_at',)

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'created_at', 'secret_token')
    readonly_fields = ('created_at', 'secret_token')
    inlines = [AnonymousCommentInline]

@admin.register(AnonymousComment)
class AnonymousCommentAdmin(admin.ModelAdmin):
    list_display = ('photo', 'content', 'created_at')
    readonly_fields = ('created_at',)
