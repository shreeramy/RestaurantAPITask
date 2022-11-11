from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from base.utils import get_today
from base.messages import Messages
from django. db. models import Sum
from ..models import DailyMenu, MainMenu, Feedback
from .serializers import (
    DailyMenuCreateSerializer, 
    FeedbackSerializer,
    MainMenuCreateSerializer
    )


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
                                               days__date=get_today())
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
            queryset = Feedback.objects.filter(
                restraunt=request.\
                data['restraunt'],
                created_at__date=get_today(),
                email=request.data['email']).exists()
            if not queryset:
                serializer = self.serializer_class(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(Messages.FEEDBACK, 
                                    status=status.HTTP_201_CREATED)
                return Response(serializer.errors, 
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(Messages.FEEDBACK_NOT_SUBMIT,
                                status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            return Response(str(e), status=status.\
                            HTTP_500_INTERNAL_SERVER_ERROR)


class FeedbackListView(APIView):
    serializer_class = FeedbackSerializer

    def get(self, request):
        restraunt = request.query_params.get('restraunt')
        queryset = Feedback.objects.filter(created_at__date=get_today(),
                                           restraunt=restraunt) 
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TopMenuListView(APIView):
    serializer_class = FeedbackSerializer

    def get(self, request):
        qr = Feedback.objects.values('restraunt').annotate(vote_count=
                            Sum('vote')).order_by('-vote_count')[:3]
        feedback_data = [i['restraunt'] for i in qr]
        serializer = self.serializer_class(feedback_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


