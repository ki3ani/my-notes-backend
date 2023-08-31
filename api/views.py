from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from api.serializer import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import Note, CustomUser
from .serializer import NoteSerializer, ProfileSerializer


# Create your views here.

#Login User
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

#Register User
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/',
        '/api/prediction/'
        'api/notes/',
        'api/note/<int:pk>/',
        'api/note/<int:pk>/update/',
        'api/note/<int:pk>/delete/',
        'api/note/mynotes/',
        'api/notes/create/',
        'api/profile/',
        'api/profile/update/',
        'api/users/<int:pk>/notes',

    ]
    return Response(routes)

#api/notes
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    public_notes = Note.objects.filter(is_public=True).order_by('-updated')[:10]
    user_notes = request.user.notes.all().order_by('-updated')[:10]
    notes = public_notes | user_notes
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


#api/notes/<int:pk>
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNote(request, pk):
    note = request.user.notes.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


#api/notes/<int:pk>/update
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def updateNote(request, pk):
    note = request.user.notes.get(id=pk)
    serializer = NoteSerializer(instance=note, data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



#api/notes/<int:pk>/delete
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteNote(request, pk):
    note = request.user.notes.get(id=pk)
    note.delete()
    return Response('Note was deleted')


#api/notes/create
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createNote(request):
    user = request.user
    data = request.data
    note = Note.objects.create(
           user=user,
        title=data['title'],
        body=data['body'],
        cover_image=data['cover_image']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


#api/profile  and api/profile/update
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request):
    user = request.user
    serializer = ProfileSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def updateProfile(request):
    user = request.user
    serializer = ProfileSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



#api/notes/user/<int:pk>/mynotes
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserNotes(request, pk):
    user = CustomUser.objects.get(id=pk)
    notes = Note.objects.filter(user=user)
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

