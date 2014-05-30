import datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView
from django.views.generic.edit import FormView


from .models import Post, Comment
from .forms import PostCreateForm, CommentCreateForm


class Login(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"

    def get_success_url(self):
        return reverse_lazy('main')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return HttpResponseRedirect(reverse_lazy('main'))


class PostList(ListView):
    template_name = "blog.html"
    queryset = Post.objects.order_by('-pub_date')
    context_object_name = "posts"  # El nombre que tendra nuestra lista en el
                                   # template (para el for)


class PostCreate(CreateView):
    form_class = PostCreateForm
    template_name = "post_create.html"
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.created_by = self.request.user
        post.pub_date = datetime.datetime.now()

        return super(PostCreate, self).form_valid(form)


class PostDetails(CreateView):
    form_class = CommentCreateForm
    template_name = "post_details.html"

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.pub_date = datetime.datetime.now()

        return super(PostDetails, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PostDetails, self).get_context_data(**kwargs)
        post = Post.objects.get(id=self.kwargs['post_id'])
        context['post'] = post
        context['comments'] = Comment.objects.filter(post=post).order_by('-pub_date')
        return context

    def get_success_url(self):
        return reverse_lazy('post_details', kwargs=self.kwargs)
