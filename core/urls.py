from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('blog-detail/', views.blogdetail, name='blogdetail'),
]


# urlpatterns = [
#     # post views
#     # path('', views.post_list, name='post_list'),
#     path('', views.PostListView.as_view(), name='post_list'),
#     # works since slugField has unique_for_date parameter
#     path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
# ]