from django.urls import path
from .views import ( ArticleListView,ArticleDetailView,SearchListView)

app_name='blog'
urlpatterns = [
    path('', ArticleListView.as_view(), name='blog'),
    path('search/', SearchListView.as_view(), name='search_list'),  # Add this for search
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),  # Use slug

    # path('', ArticleList.as_view(), name='blog'),
    # path('article/<slug:slug>',ArticleDetail.as_view(), name='article_detail'),
    # path('category/<slug:slug>',CateogryList.as_view(), name='category'),
    # path('search/', SearchList.as_view(), name='search'),
    # path('search/page/<int:page>', SearchList.as_view(), name="search")

]
