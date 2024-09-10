from django.conf import settings
from django.core.management.base import BaseCommand
import psycopg2
from rdflib import (
    plugin,
    Graph,
    Literal,
    URIRef,
    ConjunctiveGraph,
    Namespace,
    RDF,
)
from rdflib.namespace import (
    Namespace,
    RDF,
    XSD,
    FOAF,
)
from rdflib.plugins.stores.sparqlstore import SPARQLStore
from rdflib.store import Store
import rdflib_sqlalchemy


class Command(BaseCommand):
    help = "Setup RDF Alchemy"

    def setup_rdfalchemy(self) -> None:
        """Setup RDF Alchemy"""

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

        # Create triples
        bob = URIRef("http://example.org/people/Bob")

        # RDF.type: instance of a class
        """
        First triple: Bob is of type foaf:Person.
        Second triple: Bob"s name is "Bob".
        Third triple: Bob"s age is 30, with the age datatype specified as an integer.
        """
        graph.add((bob, RDF.type, FOAF.Person)) # stored in type_statements table
        graph.add((bob, FOAF.name, Literal("Bob"))) # stored in literal_statement table
        graph.add((bob, FOAF.age, Literal(30, datatype=XSD.integer))) # stored in literal_statement table

        # Serialize the graph to a file or output
        graph.serialize(format="turtle")

        # Define a SPARQL query to retrieve names and ages of all individuals in the RDF graph who are of type foaf:Person.
        """
        Check the type_statements table for entities that are of type foaf:Person.
        Then join these results with the literal_statements table to find matching foaf:name and foaf:age literals.

        The SPARQL engine will generate SQL queries that perform joins between the relevant tables using the "subject column as the common key." Here’s an example of how the joins might look in SQL:
        """
        """
        SQL

        SELECT ls1.object AS name, ls2.object AS age
        FROM type_statements ts
        JOIN literal_statements ls1 ON ts.member = ls1.subject
        JOIN literal_statements ls2 ON ts.member = ls2.subject
        WHERE ts.klass = "http://xmlns.com/foaf/0.1/Person"
        AND ls1.predicate = "http://xmlns.com/foaf/0.1/name"
        AND ls2.predicate = "http://xmlns.com/foaf/0.1/age";

        """
        query = """
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        SELECT ?name ?age
        WHERE {
        ?person a foaf:Person ;
                foaf:name ?name ;
                foaf:age ?age .
        }
        """

        # Execute the query
        for row in graph.query(query):
            self.stdout.write(f"Name: {row.name}, Age: {row.age}")


    def handle(self, *args, **kwargs):
        """Just do it."""
        self.setup_rdfalchemy()
