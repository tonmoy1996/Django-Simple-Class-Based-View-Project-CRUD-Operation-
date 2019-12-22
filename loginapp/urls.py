from django.urls import path
from loginapp import views
from django.conf.urls import url

app_name="loginapp"

urlpatterns = [
    
    path('',views.indexView.as_view()),
    path('list',views.SchoolList.as_view(),name="list"),
    path('<slug:pk>/',views.schoolDetailview.as_view(),name="detail"),
    #url(r'^(?P<pk>\d+)/$',views.schoolDetailview.as_view(),name='detail'),
    path('create',views.schoolCreateView.as_view(),name="create"),
    path('update/<slug:pk>/',views.SchoolUpdateView.as_view(),name="update"),
    path('delete/<slug:pk>/',views.SchoolDeleteView.as_view(),name="delete")
]