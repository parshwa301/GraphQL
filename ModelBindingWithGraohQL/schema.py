import graphene
from ModelBindingWithGraohQL.models.model import *
from ModelBindingWithGraohQL.query import *
import json


class GraphQL:
    def __init__(self):
        self.schema = graphene.Schema(
            esmaquery=Query,
            types=[Firds, Fitrs]
        )
        print(self.schema)



    def graphquery(self, query):
        # results = self.schema.execute(query, middleware=[timing_middleware,AuthorizationMiddleware()]) #authorization_middleware])
        results = self.schema.execute(query)
        return json.dumps(results.data)