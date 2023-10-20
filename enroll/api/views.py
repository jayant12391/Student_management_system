from enroll.models import User
from enroll.api.serializers import UserSerializer
from rest_framework import viewsets
# from rest_framework.authentication import SessionAuthentication        ###### this is for Authentication purpose only authentication 
# from rest_framework.permissions import IsAuthenticatedOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [SessionAuthentication]    
    # permission_classes = [IsAuthenticatedOrReadOnly]



