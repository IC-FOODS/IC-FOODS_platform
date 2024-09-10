import time

from django.core.management.base import BaseCommand
import psycopg2
from rdflib import plugin, Graph, Literal, URIRef
from rdflib.store import Store
import rdflib_sqlalchemy



class Command(BaseCommand):
    help = ""

    def run_ppod(self) -> None:
        """Run PPOD import"""

        # Register SQLAlchemy plugins for RDFLib
        rdflib_sqlalchemy.registerplugins()

        # Define the connection URI for the PostgreSQL database
        dburi = URIRef('postgresql+psycopg2://postgres:postgres@localhost/rdfgraph')

        # Define the RDF graph identifier
        ident = URIRef('http://example.org/test')

        # Initialize the store and the graph using the SQLAlchemy plugin
        store = plugin.get('SQLAlchemy', Store)(identifier=ident)
        graph = Graph(store, identifier=ident)

        # Open the database connection
        graph.open(dburi, create=True)

        # Measure the start time
        start_time = time.time()

        # Load the RDF data from the file into the graph
        rdf_file_path = 'PPOD/PPOD_CA.ttl'  # Replace with the actual file path
        graph.parse(rdf_file_path, format='turtle')

        # Measure the end time
        end_time = time.time()

        # Calculate the elapsed time
        elapsed_time = end_time - start_time

        # Print the elapsed time
        self.stdout.write(f"Elapsed time: {elapsed_time} seconds")



    def handle(self, *args, **kwargs):
        """Just do it."""
        self.run_ppod()
