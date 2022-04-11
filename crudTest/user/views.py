import jwt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from user.models import User
from user.serializers import UserSerializer
from rest_framework.decorators import api_view


# register method
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        userserializer = UserSerializer(data=data)
        message = "User {} successfully registered!".format(data['username'])
        if userserializer.is_valid():
            userserializer.save()
            return JsonResponse({'message': message},
                                status=status.HTTP_200_OK)

        else:
            return JsonResponse({'message': 'fail'},
                                status=status.HTTP_400_BAD_REQUEST)

    else:
        return JsonResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


# login method
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        username = data['username']
        password = data['password']
        try:
            user = User.objects.get(username=username, password=password)
            print(user.id)
            encoded = jwt.encode({'username': username}, 'applesaucepenguin',
                                 algorithm='HS256')
            request.session[username + 'token'] = encoded
            return JsonResponse({
                'message': 'Success',
                'userid': user.id,
                'token': encoded
                },
                status=status.HTTP_200_OK
            )

        except User.DoesNotExist:
            return JsonResponse(
                {'message': 'Invalid username or password'},
                status=status.HTTP_404_NOT_FOUND
            )

    else:
        return JsonResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


# logout methof
@api_view(['GET'])
def logout(request, pk):
    if request.method == 'GET':
        username = User.objects.get(pk=pk).username
        token = request.session.get(username + 'token')
        print(token)
        try:
            del request.session[username + 'token']
            return JsonResponse(
                {'message': 'Success'},
                status=status.HTTP_200_OK)

        except KeyError:
            return JsonResponse(
                {'message': 'Bad Request'},
                status=status.HTTP_400_BAD_REQUEST)

    else:
        return JsonResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)
