from django.core.mail import send_mail
from django.shortcuts import render, redirect

from django.views.generic import ListView, DetailView


from .models import Post
from .forms import ContactForm
from django.conf import settings


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post/index.html'
    paginate_by = 4


class OlderPostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post/older_posts.html'
    paginate_by = 4

class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post/post.html'


class PostAbout(ListView):
    model = Post
    template_name = 'post/about.html'


def contacts(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            mail = send_mail(
                form.cleaned_data['email'],
                form.cleaned_data['message'],
                settings.EMAIL_HOST_USER,
                ['finchchanneltm@gmail.com'],
                fail_silently=False,
                html_message='<h2>Сообщение:</h2><br>' + form.cleaned_data['message'] + '<br>' + '<h2>Имя:</h2>' +
                             form.cleaned_data['name']
            )
            if mail:
                context = {'success': 1}
                return redirect('contact')
            else:
                context = {'error': 0}
    else:
        form = ContactForm()
    context['form'] = form
    return render(request, 'post/contact.html', context=context)

