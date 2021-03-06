import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from schema import Query

app = FastAPI()

app.add_route('/graphql', GraphQLApp(schema=graphene.Schema(query=Query)))

@app.get('/')
def ping():
    return {'msg': 'My first commit'}