from django.urls import path
from .views import *

urlpatterns = [
    path('category/', CategoryList.as_view()),
    path('category/<int:pk>/', CategoryDetail.as_view()),
    path('name/', NameList.as_view()),
    path('name/<int:pk>/', NameDetail.as_view()),
    path('name/by_category/<int:category_id>/', NameByCategoryList.as_view()),
    path('name/by_city/<str:city>/', NameByCityList.as_view()),
    path('name/search_by_address/<str:address>/', NameSearchByAddressList.as_view()),
    path('name/search_by_name/<str:name>/', NameSearchByNameList.as_view()),
]