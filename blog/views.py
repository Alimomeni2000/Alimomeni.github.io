from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Article, Category, Comment, ArticleHit, IPAddress
from .forms import CommentForm, ArticleForm  # Ensure ArticleForm is imported


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'
    paginate_by = 9  # Pagination for 3 articles per page

    def get_queryset(self):
        # Filter to only return published articles and use select_related for efficiency
        return Article.objects.select_related('category').filter(status='p')
    

    
def get_client_ip(request):
    """Function to get the real client's IP address."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article, slug=slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()

        # Get the client IP address
        client_ip = get_client_ip(self.request)

        # Ensure the IP address is tracked and hits are recorded
        ip_address, created = IPAddress.objects.get_or_create(ip_address=client_ip)
        hit, hit_created = ArticleHit.objects.get_or_create(article=article, ip_address=ip_address)

        # If the hit was created (i.e., new hit), increment the view count
        context['hit_count'] = article.hit_count()

        # Fetch and display top-level comments
        context['comments'] = article.comments.filter(parent=None)
        context['form'] = CommentForm()

        return context

    def post(self, request, *args, **kwargs):
        article = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article

            # Handle replies by checking for parent comment
            parent_id = request.POST.get('parent_id')
            if parent_id:
                parent_comment = get_object_or_404(Comment, id=parent_id)
                comment.parent = parent_comment

            comment.save()
            return redirect('blog:article_detail', slug=article.slug)

        return self.get(request, *args, **kwargs)

class CategoryListView(ListView):
    template_name = "blog/category.html"
    paginate_by = 9

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        self.category = get_object_or_404(Category.objects.active(), slug=slug)
        return self.category.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


class SearchListView(ListView):
    template_name = "blog/search_list.html"
    paginate_by = 9

    def get_queryset(self):
        search_term = self.request.GET.get('q')
        return Article.objects.filter(Q(content__icontains=search_term) | Q(title__icontains=search_term))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q')
        return context


# View to Create Articles with Image Upload Support
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_form.html'  # Template for article creation
    success_url = '/success/'  # Redirect after a successful submission

    def form_valid(self, form):
        form.instance.author = self.request.user  # Optionally, associate the article with the logged-in user
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    
class SearchListView(ListView):
    model = Article
    template_name = "blog/search_list.html"  # You need to create this template
    context_object_name = 'articles'
    paginate_by = 9

    def get_queryset(self):
        search_term = self.request.GET.get('q')
        return Article.objects.filter(Q(content__icontains=search_term) | Q(title__icontains=search_term))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q')
        return context