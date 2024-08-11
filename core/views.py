from rest_framework.decorators import api_view
from rest_framework.response import Response
import pickle
from rest_framework import status
import os

@api_view(['GET'])
def predictLaptopPrice(request):
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    file_path = os.path.join(parent_dir, 'predictionFunction.pkl')
    print("File path:", file_path)
    with open(file_path, 'rb') as file:
        predictionFunction = pickle.load(file)
        file.close()
    print("Loaded prediction function:", predictionFunction)
    processor_speed = request.GET.get('processor_speed')
    ram_size = request.GET.get('ram_size')
    storage_capacity = request.GET.get('storage_capacity')
    result = predictionFunction([[processor_speed, ram_size, storage_capacity]])
    return Response({'price': result[0]}, status=status.HTTP_200_OK)
