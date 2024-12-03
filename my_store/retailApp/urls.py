from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('users',views.user,name='users'),
    path('newUser',views.NewUser,name='newUser'),
    path('inventory',views.inventory,name='Inventory'),
    path('product_detail',views.product_detail,name ='product-desc'),
    path('test',views.test,name='test'),
    path('expense_tracker',views.expense,name='expense'),
    path('jobs',views.jobs,name='jobs'),
    path('library',views.library,name='library'),
    path('img_edit',views.image,name='img-edit'),
    path('docs',views.docs,name='docs'),
    path('scrapper',views.scrapper,name='scrapper'),
    path('analytics',views.analytics,name='analytics'),
    path('booking',views.booking,name='booking'),
    path('library/books',views.books,name='books',)
]