from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Post
from .filters import PostFilter
from django_filters.views import FilterView
from .forms import NewsEditForm, NewsAddForm, ArticleAddForm
from django.contrib.auth.decorators import login_required
from django.db.models import Exists, OuterRef
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import Subscriber, Category




class PostsList(ListView):
    model = Post
    template_name ='news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-time_create')
    paginate_by = 10


class PostDetail(DetailView):
    template_name = 'news_detail.html'
    queryset = Post.objects.all()


class PostEdit(UpdateView, PermissionRequiredMixin):
    permission_required = ('news.news_edit',)
    model = Post
    template_name = 'news_edit.html'
    form_class = NewsEditForm


class Search(FilterView):
    model = Post
    context_object_name = 'search'
    template_name = 'search.html'
    filterset_class = PostFilter


class PostDelete(DeleteView, PermissionRequiredMixin):
    permission_required = ('news.post_add',)
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('')


class PostCreate(CreateView, PermissionRequiredMixin):
    permission_required = ('news.post_add',)
    raise_exception = True
    model = Post
    template_name = 'news_add.html'
    form_class = NewsAddForm


class CreateAR(CreateView, PermissionRequiredMixin):
    permission_required = ('news.add_news',)
    model = Post
    template_name = 'news_add.html'
    form_class = ArticleAddForm

    def form_valid(self, form):
            post = form.save(commit=False)
            post.post_type = 'AR'
            return super().form_valid(form)


@login_required
@csrf_protect
def subscriptions(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        action = request.POST.get('action')

        if action == 'subscribe':
            Subscriber.objects.create(user=request.user, category=category)
        elif action == 'unsubscribe':
            Subscriber.objects.filter(
                user=request.user,
                category=category,
            ).delete()

    categories_with_subscriptions = Category.objects.annotate(
        user_subscribed=Exists(
            Subscriber.objects.filter(
                user=request.user,
                category=OuterRef('pk'),
            )
        )
    ).order_by('pk')
    return render(
        request,
        'subscriptions.html',
        {'categories': categories_with_subscriptions},
    )