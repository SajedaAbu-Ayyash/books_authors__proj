from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	
    path('add_book', views.add_book),  
    path('submit_book', views.submit_book),
    path('books/<int:book_id>', views.book),
    path('books/<int:book_id>/add_author_to_book', views.add_author_to_book),
    path('add_author', views.add_author),
    path('submit_author', views.submit_author),
    path('authors/<int:author_id>', views.author),
    path('authors/<int:author_id>/add_book_to_author', views.add_book_to_author)
]
