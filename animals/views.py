from logging import raiseExceptions
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status

from animals.models import Animal
from animals.serializers import AnimalSerializer

# Create your views here.
class AnimalView(APIView):
    def get(self, response: Response):
        get_animals = Animal.objects.all()

        serializer = AnimalSerializer(get_animals, many=True)
        
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request):
        try:
            send_animal = AnimalSerializer(data=request.data)
            send_animal.is_valid(raise_exception=True)

            send_animal.save()

            return Response(send_animal.data, status.HTTP_201_CREATED)

        except IntegrityError:
            return Response({"error": "Animal already exists"}, status.HTTP_409_CONFLICT)

    
class AnimalIDView(APIView):
    def get(self, _: Request, animal_id: int):
        try:
            get_animal = get_object_or_404(Animal, pk=animal_id)

            serializer = AnimalSerializer(get_animal)

            return Response(serializer.data, status.HTTP_200_OK)
        
        except:
            return Response({"message": "Animal Not Found."}, status.HTTP_404_NOT_FOUND)


    def patch(self, request: Request, animal_id: int):
        try:
            get_animal = get_object_or_404(Animal, pk=animal_id)

            serializer = AnimalSerializer(get_animal, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data)

        except KeyError as e:
            return Response(e.args, status.HTTP_422_UNPROCESSABLE_ENTITY)


    def delete(self, _: Request, animal_id: int):
        try:
            get_animal = get_object_or_404(Animal, pk=animal_id)

            get_animal.delete()

            return Response("", status.HTTP_204_NO_CONTENT)
        
        except:
            return Response({"message": "Animal Not Found."}, status.HTTP_404_NOT_FOUND)