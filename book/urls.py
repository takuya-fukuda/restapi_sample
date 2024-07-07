from django.urls import path
from .views import BookList, Topview, WeatherDetailView, BookListAPI, SampleAPI


urlpatterns = [
    path('list/', BookList.as_view()),
    path('top/', Topview.as_view()),
    path('detail/<int:pk>/', WeatherDetailView.as_view()),
    path('api/', BookListAPI.as_view()),
    path('api2/', SampleAPI.as_view()),
]