from django.urls import path

from .import views

urlpatterns = [
    path('welcome/', views.WelcomeView.as_view()),
    path('livros/', views.BooksView.as_view()),
    path('author/', views.AuthorCreateView.as_view()),
    path('livro/', views.BookCreateView.as_view()),
    path('detalhe/<int:pk>/', views.BoolDetailView.as_view()),
    path('detalhecode/<int:code>/', views.BookDetailByCodeView.as_view())
]