from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Client
from .permissions import IsOwnerOrReadOnly
from .serializers import ClientSerializer


class ListCreateClientAPIView(ListCreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Assign the user who created the client
        serializer.save(creator=self.request.user)

class RetrieveUpdateDestroyClientAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]






