from django.shortcuts import render

# Create your views here.
from ninja import NinjaAPI

router = NinjaAPI()


@router.get("/hello")
def hello(request):
    return {"message": "Hello, world!"}