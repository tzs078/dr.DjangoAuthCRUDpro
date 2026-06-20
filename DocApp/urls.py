
from django.urls import path
from DocApp.views import *

urlpatterns = [
   path('homePage/',homePage , name='homePage'),
   path('homeDetailsPage/<str:id>/', homeDetailsPage, name='homeDetailsPage'),
   # CURD 
   path('docListPage/',docListPage , name='docListPage'),
   path('docAddPage/',docAddPage , name='docAddPage'),
   path('docDltPage/<str:id>/',docDltPage, name='docDltPage'),
   path('docUpdatePage/<str:id>/',docUpdatePage, name='docUpdatePage'),
   # auth 
   path('', signupPage , name='signupPage'),
   path('loginPage/', loginPage , name='loginPage'),
   path('logoutPage/',logoutPage, name='logoutPage'),
]
