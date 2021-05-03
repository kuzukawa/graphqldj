from graphene import ObjectType, Schema

from books.graphql.schema import Query as InfoQuery
from books.graphql.schema import Mutation as InfoMutation


class Query(InfoQuery, ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation(InfoMutation, ObjectType):
    # This class will inherit from multiple Mutations
    # as we begin to add more apps to our project
    pass


schema = Schema(query=Query, mutation=Mutation)