from lib2to3.pgen2 import token
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView




from .serializers import NoteSerializer
from base.models import Note


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    # @classmethod
    # def get_token(cls, user):
    #     token = super().get_token(user)

    #     # Add custom claims
    #     token['username'] = user.username
    #     # from backend.script.script_login_modeus import loginMOD
    #     # loginMOD(user.username, user.password)
        
    #     return token
    
    @classmethod
    def hello(request):   
        from script.script_login_modeus import loginMOD
        token = loginMOD(request.data['username'], request.data['password'])
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
       
#         '/api/token/refresh',
#     ]

#     return Response(routes)


@api_view(['GET'])
def getNotes(request):
    user = request.user
    notes = user.note_set.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

# @api_view(['POST'])
# def hello_world(request):   
#     from script.script_login_modeus import loginMOD
#     token = loginMOD(request.data['username'], request.data['password'])
#     return Response(token)

   