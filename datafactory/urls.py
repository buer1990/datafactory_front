from django.urls import path

from datafactory import views

app_name = 'datafactory'
urlpatterns = [
    path('<int:tool_id>/', views.detail, name="detail"),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:tool_id>/tool', views.create_data, name="tool"),

]