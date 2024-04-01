from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Comment, Subscription, PostPhoto
from django.db.models import Q
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.contrib.auth import logout
from .forms import CommentForm
from .forms import SubscriptionForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def get_categories():
    all = Category.objects.all()
    count = all.count()
    half = count / 2 + count % 2
    return {'cats1': all[:half], 'cats2': all[half:]}


def index(request):
    posts = Post.objects.all().order_by("-published_date")
    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    # posts = paginator.page(page)
    context = {"posts": posts}
    context.update(get_categories())
    return render(request, 'blog/index.html', context)


def post(request, title=None):

    post = get_object_or_404(Post, title=title)
    imgs = PostPhoto.objects.filter(post=post)
    context = {"post": post, "imgs": imgs}
    context.update(get_categories())
    return render(request, 'blog/post.html', context)


def about(request):
    context = {}
    context.update(get_categories())
    return render(request, 'blog/about.html', context)


def contact(request):
    context = {}
    context.update(get_categories())
    return render(request, 'blog/contact.html', context)


def category(request, name=None):
    c = get_object_or_404(Category, name=name)
    posts = Post.objects.filter(category=c).order_by("-published_date")
    context = {"posts": posts}
    context.update(get_categories())
    return render(request, 'blog/index.html', context)


def tags(request, title=None):
    tags = get_object_or_404(Post, title=title)
    context = {'tags': tags}
    return render(request, 'blog/index.html', context)


def get_tags():
    all = Category.objects.all()
    return {all}

# def comment(request, title=None):
#     comment = get_object_or_404(Post, title=title)
#     context = {'comment': comment}
#     return render(request, 'blog/post.html', context)


# def comment(request):
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.published_date = now()
#             comment.user = request.user
#             comment.save()
#             return index(request)
#     form = CommentForm()
#     context = {"form": form}
#     context.update(get_categories())
#     return render(request, 'blog/comment.html', context)


def search(request):
    query = request.GET.get('query')
    posts = Post.objects.filter(Q(content__icontains=query) | Q(title__icontains=query))
    context = {"posts": posts}
    context.update(get_categories())
    return render(request, 'blog/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = now()
            post.user = request.user
            post.save()
            return index(request)
    form = PostForm()
    context = {"form": form}
    context.update(get_categories())
    return render(request, 'blog/create.html', context)

def subscription(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save(commit=False)
            subscription.published_date = now()
            subscription.user = request.user
            subscription.save()
            return index(request)
    form = SubscriptionForm()
    context = {"form": form}
    context.update(get_categories())
    return render(request, 'blog/subscription.html', context)

def comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.published_date = now()
            comment.user = request.user
            comment.save()
            return index(request)
    form = CommentForm()
    context = {"form": form}
    context.update(get_categories())
    return render(request, 'blog/comment.html', context)

def logout_view(request):
    logout(request)

#
#
# def comment(request, year, month, day, post):
#     post = get_object_or_404(Post, slug=post,
#                              status='published',
#                              publish__year=year,
#                              publish__month=month,
#                              publish__day=day)

# def comment(request):
#     post = get_object_or_404(Post)
#     # Список активных комментариев к этой записи
#     comments = post.comments.filter(active=True)
#     new_comment = None
#     context = {"comment": comment}
#     if request.method == 'POST':
#         # Комментарий был опубликован
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             # Создайте объект Comment, но пока не сохраняйте в базу данных
#             new_comment = comment_form.save(commit=False)
#             # Назначить текущий пост комментарию
#             new_comment.post = post
#             # Сохранить комментарий в базе данных
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#     return render(request, 'blog/create.html', context)
# return render(request,
#                   'blog/comment.html',
#                   {'post': post,
#                    'comments': comments,
#                    'new_comment': new_comment,
#                    'comment_form': comment_form})


# def comment(request):
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.created = now()
#             comment.updated = now()
#             comment.save()
#             return index(request)
#     form = CommentForm()
#     context = {"form": form}
#     context.update(get_categories())
#     return render(request, 'blog/index.html', context)
    #
    #
    # if request.method == 'POST':
    #     form = CommentForm(request.POST)
    #     post = get_object_or_404(Post, pk=pk, slug=slug)
    #     comments = post.comment_set.all()
    #
    # context['post'] = post
    # context['comments'] = comments
    # context['form'] = form
    # return context
    #
    #
    # if request.method == 'POST':
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.published_date = now()
    #         post.save()
    #         return index(request)
    # form = PostForm()
    # context = {"form": form}
    # context.update(get_categories())
    # return render(request, 'blog/deteil.html', context)

    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     pk = self.kwargs["pk"]
    #     slug = self.kwargs["slug"]
    #
    #     form = CommentForm()
    #     post = get_object_or_404(Post, pk=pk, slug=slug)
    #     comments = post.comment_set.all()
    #
    #     context['post'] = post
    #     context['comments'] = comments
    #     context['form'] = form
    #     return context
    #
    # def post(self, request, *args, **kwargs):
    #     form = CommentForm(request.POST)
    #     self.object = self.get_object()
    #     context = super().get_context_data(**kwargs)
    #
    #     post = Post.objects.filter(id=self.kwargs['pk'])[0]
    #     comments = post.comment_set.all()
    #
    #     context['post'] = post
    #     context['comments'] = comments
    #     context['form'] = form
    #
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         email = form.cleaned_data['email']
    #         content = form.cleaned_data['content']
    #
    #         comment = Comment.objects.create(
    #             name=name, email=email, content=content, post=post
    #         )
    #
    #         form = CommentForm()
    #         context['form'] = form
    #         return self.render_to_response(context=context)
    #
    #     return self.render_to_response(context=context)
