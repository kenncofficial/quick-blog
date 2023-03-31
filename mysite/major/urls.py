from django.urls import path
from .views import HomeView, AboutView, WorkView # PortfolioDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('work', WorkView.as_view(), name='work')
  #  path('portfolio/<int:pk>', PortfolioDetailView.as_view(), name='portfolio-details'),
]