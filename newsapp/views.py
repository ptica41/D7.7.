from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy


class Search(ListView):
    queryset = Post.objects.filter(type=0)
    ordering = '-time'
    template_name = 'search.html'
    context_object_name = 'search'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class News(ListView):
    queryset = Post.objects.filter(type=0)
    ordering = '-time'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        a = Post.objects.all()
        context['amount'] = 0
        for i in a:
            if i.type == 0:
                context['amount'] += 1
        return context


class NewsDetail(DetailView):
    queryset = Post.objects.filter(type=0)
    template_name = 'new.html'
    context_object_name = 'new'


class NewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'createnews.html'


class NewsUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'createnews.html'


class NewsDelete(DeleteView):
    model = Post
    template_name = 'deletenews.html'
    success_url = reverse_lazy('news_list')


class Articles(ListView):
    queryset = Post.objects.filter(type=1)
    ordering = '-time'
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        a = Post.objects.all()
        context['amount'] = 0
        for i in a:
            if i.type == 1:
                context['amount'] += 1
        return context


class Article(DetailView):
    queryset = Post.objects.filter(type=1)
    template_name = 'article.html'
    context_object_name = 'article'


class ArticlesSearch(ListView):
    queryset = Post.objects.filter(type=1)
    ordering = '-time'
    template_name = 'articlessearch.html'
    context_object_name = 'search'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ArticlesCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'createarticles.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 1
        return super().form_valid(form)


class ArticlesUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'createarticles.html'


class ArticlesDelete(DeleteView):
    model = Post
    template_name = 'deletearticles.html'
    success_url = reverse_lazy('articles_list')