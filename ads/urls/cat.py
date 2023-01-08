from django.urls import path

from ads.views.cat import CategoriesView, CategoryViewDetail, CategoryUpadeteView, CategoryDeleteView

urlpatterns = [



    path('cat/', CategoriesView.as_view(), name="CategoriesView"),
    path('cat/<int:pk>/', CategoryViewDetail.as_view(), name='CategoryViewDetail'),
    path('cat/<int:pk>/update/', CategoryUpadeteView.as_view()),
    path('cat/<int:pk>/delete/', CategoryDeleteView.as_view()),


]