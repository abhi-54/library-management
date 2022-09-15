from rest_framework.response import Response
from rest_framework.decorators import api_view
from library_app.models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def api_all_links(request):
	api_urls = {
		'List All Books':'/api/all-books/',
		'Detail Book View':'/api/book/<int:id>/',
		'Create Book':'/api/create-book/',
		'Update Book':'/api/update-book/<int:id>/',
		'Delete Book':'/api/delete-book/<int:id>/',
		}
	return Response(api_urls)

@api_view(['GET'])
def allBooks(request):
  books = Book.objects.all()
  serializer = BookSerializer(books, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def book(request, id):
  book = Book.objects.get(id=id)
  serializer = BookSerializer(book)
  return Response(serializer.data)

@api_view(['POST'])
def create_book(request):
  serializer = BookSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

@api_view(['POST'])
def update_book(request, id):
  book = Book.objects.get(id=id)
  serializer = BookSerializer(instance=book, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

@api_view(['DELETE'])
def delete_book(request, id):
  book = Book.objects.get(id=id)
  book.delete()
  return Response('Deleted Successfully')