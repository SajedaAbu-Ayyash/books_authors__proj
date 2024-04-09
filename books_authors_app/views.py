from django.shortcuts import render, redirect
from . import models

#this function will display the main page"home page"
def index(request):
    return render(request, 'index.html')

#this function will display all books in db 
def add_book(request):
    context = {
        'books': models.display_books()
    }
    return render(request, 'add_book.html', context)

#this function will add new book to db
def submit_book(request):
    if request.method == 'POST':
        models.submit_book(request)
        return redirect('/add_book')

#this function will get book by id yo show the book details  
def book(request, book_id):
    context = {
        'book': models.Book.objects.get(id=book_id),
        'authors': models.Author.objects.exclude(id = book_id) 
    }
    return render(request, 'book_details.html', context)

#this function to add authors to specific book
def add_author_to_book(request, book_id):
    if request.method == 'POST':
        models.add_author_to_book(request, book_id)
        return redirect(f"/books/{book_id}")

#this function will display all books in db 
def add_author(request):
    context= {
        'authors': models.Author.objects.all()
    }
    return render(request, 'add_author.html', context)

#this function will add new author to db
def submit_author(request):
    if (request.method == "POST"):
        models.submit_author(request)
        return redirect('/add_author')
    
#this function will get author by id yo show the author details  
def author(request, author_id):
    author = models.Author.objects.get(id = author_id)
    context = {
        'author' : models.Author.objects.get(id = author_id),
        'books' : models.Book.objects.exclude(authors = author)
    }
    return render(request, 'author_details.html', context)

#this function to add books to specific author
def add_book_to_author(request, author_id):
    if request.method == 'POST':
        models.add_book_to_author(request.POST, author_id)
        return redirect(f"/authors/{author_id}")




# Create your views here.
