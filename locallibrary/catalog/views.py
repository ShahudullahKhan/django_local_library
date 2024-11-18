from django.shortcuts import render

from .models import Book, Author, BookInstance, Genre

from django.views import generic

# Create your views here.

def index(request):
    """ View function for home page of site. """

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # challenge 5 part
    num_genres = Genre.objects.count()
    book_Ring_word = Book.objects.filter(title__icontains='ring').count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The all() is implied by default
    num_authors = Author.objects.count()

    context = {
        'num_books' : num_books,
        'num_instances' : num_instances,
        'num_instances_available' : num_instances_available,
        'num_authors' : num_authors,
        'num_genres' : num_genres,
        'book_Ring_word': book_Ring_word,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3


class BookDetailView(generic.DetailView):
    model = Book



# Challenge no. 6 part
# For Author list views and detail views

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2

class AuthorDetailView(generic.DetailView):
    model = Author

