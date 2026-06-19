
from django.urls import path
from DocApp.views import *

urlpatterns = [
   path('',homePage , name='homePage'),
   path('docListPage/',docListPage , name='docListPage'),
   path('docAddPage/',docAddPage , name='docAddPage'),
   path('docDltPage/<str:id>/',docDltPage, name='docDltPage'),
   path('docUpdatePage/<str:id>/',docUpdatePage, name='docUpdatePage'),

   path('signupPage/', signupPage , name='signupPage'),
   path('loginPage/', loginPage , name='loginPage'),
   path('logoutPage/',logoutPage, name='logoutPage'),
]
