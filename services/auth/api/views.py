from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..authentication import CustomTokenAuthentication
from ..models import CustomUser
from ..serializers import UserSerializer


class UserListView(generics.ListAPIView):
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
