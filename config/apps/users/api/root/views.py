from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(http_method_names=["GET"])
def root(request):
    message = "Welcom To Mezo Backend Template!"
    return Response({"message": message})
