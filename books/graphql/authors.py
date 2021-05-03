import graphene
from graphene_django.types import DjangoObjectType, ObjectType

from ..models import Author, Book


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        
        
class Query(ObjectType):
    authors = graphene.List(AuthorType)
    
    def resolve_authors(self, info, **kwargs):
        return Author.objects.all()