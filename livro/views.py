from django.shortcuts import render

from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView

from .models import Book, Author
from .forms import BookForm, AuthorForm

#Bem vindo
class WelcomeView(TemplateView):
    template_name = 'livro/Welcome.html'


#Criando autor
class AuthorCreateView(CreateView):

    model = Author
    template_name = 'livro/criar-author.html'
    form_class = AuthorForm
    success_url = '/livraria/livros/'

#Lista de Livros
class BooksView(ListView):
     model = Book
     template_name = 'livro/Meus_livros.html'


#Criando Livros
class BookCreateView(CreateView):

    model = Book
    template_name = 'livro/criar-livros.html'
    form_class = BookForm
    success_url = '/livraria/livros/'


#Detalhes do livros
class BoolDetailView(DetailView):

    model = Book
    template_name = 'livro/detalhe-livro.html'

class BookDetailByCodeView(DetailView):
    model = Book
    template_name = 'livro/detalhe-livro.html'

    def get_object(self):
        return Book.objects.get(code=self.kwargs['code'])

#Etidar/Atualizar
class BookUpdateView(UpdateView):
    model = Book
    template_name = 'livro/editar-livro.html'
    form_class = BookForm
    success_url = '/livraria/livros'
