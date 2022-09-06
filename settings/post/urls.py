from django.urls import path
from .views import PostList, PostDetail, contacts, OlderPostList, PostAbout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('post/<int:pk>/', PostDetail.as_view(), name='detail'),
    path('contact_us/', contacts, name='contact'),
    path('older_post/', OlderPostList.as_view(), name='older'),
    path('about/', PostAbout.as_view(), name='about')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)