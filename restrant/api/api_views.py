from datetime import datetime

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from base.messages import Messages

from ..models import DailyMenu, MainMenu
from .serializers import (DailyMenuCreateSerializer, DailyMenuSerializer, FeedbackSerializer,
                          MainMenuCreateSerializer)


class MainMenuCreateView(APIView):
    serializer_class = MainMenuCreateSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(Messages.MAIN_MENU, 
                                status=status.HTTP_201_CREATED)
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.\
                            HTTP_500_INTERNAL_SERVER_ERROR)

class MainMenuView(APIView):
    serializer_class = MainMenuCreateSerializer
    permission_classes = (AllowAny,)

    def get(self, request):
        try:
            restraunt = request.query_params.get('restraunt')
            querset = MainMenu.objects.filter(restraunt=restraunt)
            serializer = self.serializer_class(querset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.\
                            HTTP_500_INTERNAL_SERVER_ERROR)


class DailyMenuCreateView(APIView):
    serializer_class = DailyMenuCreateSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(Messages.DAILY_MANU, 
                                status=status.HTTP_201_CREATED)
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.\
                            HTTP_500_INTERNAL_SERVER_ERROR)


class DailyMenuView(APIView):
    serializer_class = DailyMenuCreateSerializer
    permission_classes = (AllowAny,)

    def get(self, request):
        try:
            restraunt = request.query_params.get('restraunt')
            querset = DailyMenu.objects.filter(restraunt=restraunt, 
                            days__date=datetime.now().date())
            serializer = self.serializer_class(querset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.\
                            HTTP_500_INTERNAL_SERVER_ERROR)


class FeedbackView(APIView):
    serializer_class = FeedbackSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(Messages.FEEDBACK, 
                                status=status.HTTP_201_CREATED)
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.\
                            HTTP_500_INTERNAL_SERVER_ERROR)


class TopMenuListView(APIView):
    serializer_class = DailyMenuSerializer