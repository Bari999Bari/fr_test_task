from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Mailing


def index(request):
    template = 'mailing/index.html'
    mailing_list = Mailing.objects.all()
    paginator = Paginator(mailing_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, template, context)


def post_create(request):
    # Проверяем, получен POST-запрос или какой-то другой:
    # if request.method == 'POST':
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.author = request.user
    #         post.published_date = timezone.now()
    #         post.save()
    #         return redirect('posts:profile', username=request.user.username)
    #     return render(request, 'posts/create_post.html', {'form': form})
    # form = PostForm()
    # context = {
    #     'form': form
    # }
    # return render(request, 'posts/create_post.html', context)
    pass
