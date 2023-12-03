# artist_api/views.py

from rest_framework.authtoken.models import Token
from rest_framework import status, viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import CustomUser, Artist, Work
from .serializers import CustomUserSerializer, ArtistSerializer, WorkSerializer


class CustomUserCreate(ObtainAuthToken):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            artist = None

            artist_serializer = ArtistSerializer(
                data={"username": request.data['username'], "user": user.id})
            if artist_serializer.is_valid():
                artist = artist_serializer.save()

            work_serializer = WorkSerializer(data={
                "link": request.data.get("link"),
                "work_type": request.data.get("work_type"),
                "artist": artist.id if artist else None
            })

            if work_serializer.is_valid():
                work_serializer.save()

            token, _ = Token.objects.get_or_create(user=user)

            json = serializer.data
            json['token'] = token.key

            return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['work_type', 'artist__username']
    search_fields = ['artist__username']
    ordering_fields = ['work_type', 'artist__username']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Work.objects.all()

        work_type = self.request.query_params.get('work_type')
        if work_type:
            queryset = queryset.filter(work_type=work_type)

        artist_name = self.request.query_params.get('artist')
        if artist_name:
            queryset = queryset.filter(artist__username=artist_name)

        return queryset


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['username']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
