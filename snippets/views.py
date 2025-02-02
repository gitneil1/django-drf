from snippets.models import Snippets
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action

@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'users': reverse('user-list', request=request, format=format),
		'snippets': reverse('snippet-list', request=request, format=format)
	})

class SnippetViewSet(viewsets.ModelViewSet):
	"""
	This ViewSet automatically provides `list`, `create`, `retrieve`, `update`,
	and `destroy` actions
	Additionally we also provide an extra `highlist` action
	"""
	queryset = Snippets.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = [
		permissions.IsAuthenticatedOrReadOnly,
		IsOwnerOrReadOnly
	]

	@action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
"""
commented for ViewSet
class SnippetList(generics.ListCreateAPIView):
	queryset = Snippets.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):#create() of serializer will be triggered
		serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Snippets.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = [
		permissions.IsAuthenticatedOrReadOnly,
		IsOwnerOrReadOnly
	]

class SnippetHighlight(generics.GenericAPIView):
	queryset = Snippets.objects.all()
	renderer_classes = [renderers.StaticHTMLRenderer]

	def get(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)
"""
"""
class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
"""

class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	This viewset automatically provides `list` and `retrieve` actions.
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer









































