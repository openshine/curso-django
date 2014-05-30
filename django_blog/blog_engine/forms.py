from django import forms
from django.forms import ModelForm

from .models import Post, Comment


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')


class CommentCreateForm(ModelForm):
    post = forms.IntegerField()

    def clean_post(self):
        post_id = self.cleaned_data['post']
        post = Post.objects.get(id=post_id)
        return post

    class Meta:
        model = Comment
        fields = ('text', 'post')
