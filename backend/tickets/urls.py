from django.urls import path
from .views import TicketCreateAPIView

urlpatterns = [
    path("tickets/", TicketCreateAPIView.as_view()),
]
