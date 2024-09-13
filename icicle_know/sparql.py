from django.conf import settings
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

import rdflib_sqlalchemy
import psycopg2
from rdflib import (
    plugin,
    Graph,
    URIRef,
    Namespace,
    RDF,
)
from rdflib.namespace import Namespace
from rdflib.plugins.stores.sparqlstore import SPARQLStore
from rdflib.store import Store
import logging


log = logging.getLogger("django.log")


class SparqlAPIView(APIView):
    """SPARQL endpoint API"""
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        """SPARQL handle HTTP post"""

        # Generic namespaces
        EX = Namespace("http://example.org/")
        FOAF = Namespace("http://xmlns.com/foaf/0.1/")

        # SQLAlchemy translates the operations on RDF graphs into SQL queries that PostgreSQL understands.
        rdflib_sqlalchemy.registerplugins()

        db_username = settings.DB_USERNAME
        db_password = settings.DB_PASSWORD
        db_host = settings.DB_HOST
        db_name = settings.DB_NAME

        # SQLAlchemy uses this URI to establish a connection to the PostgreSQL database.
        dburi = URIRef(f"postgresql+psycopg2://{db_username}:{db_password}@{db_host}/{db_name}")

        # To specify RDF graph and store
        ident = URIRef("http://example.org/test")

        # Retrieves the SQLAlchemy plugin and creates an instance of it, using the "ident" identifier.
        store = plugin.get("SQLAlchemy", Store)(identifier=ident)

        # This graph will be used to store and manipulate RDF data.
        graph = Graph(store, identifier=ident)

        # Open the database connection
        graph.open(dburi, create=True)

        # Bind namespaces
        graph.bind("ex", EX)
        graph.bind("foaf", FOAF)

        sparql_query = request.data.get('query')

        log.info(sparql_query)

        result = graph.query(sparql_query)

        # Convert results to a JSON serializable format
        json_results = []
        for record in result:
            json_results.append(record)

        return Response({"results": json_results}, status=status.HTTP_200_OK)
