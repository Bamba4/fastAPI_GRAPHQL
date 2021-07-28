import graphene
from graphene.types.scalars import String


class Query(graphene.ObjectType):
    say_hello = graphene.String(name=graphene.String(default_value='Test Driven'))

    @staticmethod
    def resolve_say_hello(parent, info, name):
        return 'Hello {} .How are you ?'.format(name)

