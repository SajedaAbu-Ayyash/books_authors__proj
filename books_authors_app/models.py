from django.db import models

class Book(models.Model):
    title = models.CharField(max_length= 255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    books = models.ManyToManyField(Book, related_name='authors')
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def display_books():
   return Book.objects.all()

# this function will create new book in db
def submit_book(request):
    book = Book.objects.create(title = request.POST['title'], desc = request.POST['desc'])
    # title = post_data['title']
    # desc = post_data['desc']
    # Book.objects.create(title = post_data['title'], desc = post_data['desc'])
    

#this function will show author who added in book_details page
def add_author_to_book(request, book_id):
    print(request.POST)
    Book.objects.get(id = book_id).authors.add(Author.objects.get(id = request.POST['author_for_book']))  


def display_authors():
    return Author.objects.all()

#this function will create new author in db
def submit_author(request):
    author = Author.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], notes = request.POST['notes'])

#this function will show books who added in author_details page
def add_book_to_author(request, author_id):
    Author.objects.get(id = author_id).books.add(Book.objects.get(id = request['author_for_book']))  






    




# Create your models here.