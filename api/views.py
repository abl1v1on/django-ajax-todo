from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated

from app.models import Note
from .serializers import CreateUserSerializer, MyTokenSerializer, NoteSerializer


class MyTokenView(TokenObtainPairView):
    serializer = MyTokenSerializer


class SignUpUserView(CreateAPIView):
    serializer_class = CreateUserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny, )


class UserNotesListView(ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = NoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user, is_active=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserNoteRetriveView(RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        try:
            note = Note.objects.get(pk=kwargs['pk'])

            if note.author == request.user:
                serializer = NoteSerializer(data=note.__dict__)
                serializer.is_valid(raise_exception=True)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            return Response({'detail': 'Access is denied'}, status=status.HTTP_400_BAD_REQUEST)  
        except Note.DoesNotExist:
            return Response({'detail': 'Note not found'}, status=status.HTTP_404_NOT_FOUND)
        

    def delete(self, request, *args, **kwargs):
        try:
            note = Note.objects.get(pk=kwargs['pk'])

            if note.author == request.user:
                return super().delete(request, *args, **kwargs)
            return Response({'detail': 'Access is denied'}, status=status.HTTP_400_BAD_REQUEST)    
        
        except Note.DoesNotExist:
            return Response({'detail': 'Note not found'}, status=status.HTTP_404_NOT_FOUND)
        