from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ml.inference import predict_ticket
from .models import Ticket
from .serializers import TicketSerializer

class TicketCreateAPIView(APIView):
    def post(self, request):
        text = request.data.get("text")

        prediction = predict_ticket(text)

        ticket = Ticket.objects.create(
            text=text,
            **prediction
        )

        return Response(
            TicketSerializer(ticket).data,
            status=status.HTTP_201_CREATED
        )
