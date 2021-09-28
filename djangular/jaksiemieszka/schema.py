import graphene
from graphene.types import field, schema
from graphene_django import DjangoObjectType
from .models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "token")

class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    def resolve_all_users(root, info):
        return User.objects.all()

schema = graphene.Schema(query=Query)