from django.urls import path
from information import views



urlpatterns = [
    path('book-list',views.BookListAPIView.as_view(),name='book-list'),
    path('author-list',views.AuthorListAPIView.as_view(),name='author-list'),
    path('send-mail',views.SendMailAPIView.as_view(),name='send-mail')
    # path('test',views.Test.as_view(),name="test")
]