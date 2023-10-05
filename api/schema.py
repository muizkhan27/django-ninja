import graphene
from graphene_django.types import DjangoObjectType
from .models import Category, Task


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class TaskType(DjangoObjectType):
    class Meta:
        model = Task


class Query(graphene.ObjectType):
    all_categories = graphene.List(CategoryType)
    all_tasks = graphene.List(TaskType)

    def resolve_all_categories(self, info):
        return Category.objects.all()

    def resolve_all_tasks(self, info):
        return Task.objects.all()


schema = graphene.Schema(query=Query)
