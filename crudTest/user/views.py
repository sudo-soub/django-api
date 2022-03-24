from rest_framework.decorators import api_view
# from user.models import User
# from user.serializers import UserSerializer
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from crudTest.user.serializers import UserSerializer
from rest_framework import status


# Create your views here.
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        user = JSONParser.parse(request)
        print(user)
        return ''

    else:
        return {
            'status': 'fail',
            'message': 'Method not allowed!',
            'code': 405
        }


@api_view(['POST'])
def createuser(request):
    if request.method == 'POST':
        userdata = JSONParser.parse(request)
        user_serializer = UserSerializer(data=userdata)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    else:
        return {
            'status': 'fail',
            'message': 'Method not allowed!',
            'code': 405
        }
