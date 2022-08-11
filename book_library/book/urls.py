from django.urls import path 
from . import views

urlpatterns = [ 
    path('book/',views.ListBookView.as_view(),name = 'book-list'),
    path('book/<int:pk>/detail/',views.DetailBookView.as_view(),name = 'book-detail'),
    path('book/create/',views.CreateBookView.as_view(),name = 'book-create'),
    path('book/<int:pk>/delete/',views.DeleteBookView.as_view(),name = 'book-delete'),
    path('book/<int:pk>/update/',views.UpdateBookView.as_view(),name = 'book-update'),
]