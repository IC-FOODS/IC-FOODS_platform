from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.permissions import AllowAny

from icicle_know.models import (
    Concept,
    Relation,
    Instance,
    Proposition,
    Node,
    Edge,
)
from icicle_know.serializers import (
    ConceptSerializer,
    RelationSerializer,
    InstanceSerializer,
    PropositionSerializer,
    NodeSerializer,
    EdgeSerializer,
)

# Concept APIS
class ConceptListAPI(ListAPIView):
    """List API for Concepts"""
    permission_classes = (AllowAny,)
    queryset = Concept.objects.all()
    serializer_class = ConceptSerializer


class ConceptCreateAPI(CreateAPIView):
    """API for creating Concepts"""
    permission_classes = (AllowAny,)
    queryset = Concept.objects.all()
    serializer_class = ConceptSerializer


class ConceptViewAPI(RetrieveAPIView):
    """API for getting a single Concept"""
    permission_classes = (AllowAny,)
    serializer_class = ConceptSerializer
    queryset = Concept.objects.all()
    lookup_field = "uuid"


# Relation APIS
class RelationListAPI(ListAPIView):
    """List API for Relations"""
    permission_classes = (AllowAny,)
    queryset = Relation.objects.all()
    serializer_class = RelationSerializer


class RelationCreateAPI(CreateAPIView):
    """API for creating Relations"""
    permission_classes = (AllowAny,)
    queryset = Relation.objects.all()
    serializer_class = RelationSerializer


class RelationViewAPI(RetrieveAPIView):
    """API for getting a single Relation"""
    permission_classes = (AllowAny,)
    serializer_class = RelationSerializer
    queryset = Relation.objects.all()
    lookup_field = "uuid"


# Instance APIS
class InstanceListAPI(ListAPIView):
    """List API for Instances"""
    permission_classes = (AllowAny,)
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer


class InstanceCreateAPI(CreateAPIView):
    """API for creating Instances"""
    permission_classes = (AllowAny,)
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer


class InstanceViewAPI(RetrieveAPIView):
    """API for getting a single Instance"""
    permission_classes = (AllowAny,)
    serializer_class = InstanceSerializer
    queryset = Instance.objects.all()
    lookup_field = "uuid"


# Proposition APIS
class PropositionListAPI(ListAPIView):
    """List API for Propositions"""
    permission_classes = (AllowAny,)
    queryset = Proposition.objects.all()
    serializer_class = PropositionSerializer


class PropositionCreateAPI(CreateAPIView):
    """API for creating Propositions"""
    permission_classes = (AllowAny,)
    queryset = Proposition.objects.all()
    serializer_class = PropositionSerializer


class PropositionViewAPI(RetrieveAPIView):
    """API for getting a single Proposition"""
    permission_classes = (AllowAny,)
    serializer_class = PropositionSerializer
    queryset = Proposition.objects.all()
    lookup_field = "uuid"


# Node APIS
class NodeListAPI(ListAPIView):
    """List API for Nodes"""
    permission_classes = (AllowAny,)
    queryset = Node.objects.all()
    serializer_class = NodeSerializer


class NodeCreateAPI(CreateAPIView):
    """API for creating Nodes"""
    permission_classes = (AllowAny,)
    queryset = Node.objects.all()
    serializer_class = NodeSerializer


class NodeViewAPI(RetrieveAPIView):
    """API for getting a single Node"""
    permission_classes = (AllowAny,)
    serializer_class = NodeSerializer
    queryset = Node.objects.all()
    lookup_field = "uuid"


# Edge APIS
class EdgeListAPI(ListAPIView):
    """List API for Edges"""
    permission_classes = (AllowAny,)
    queryset = Edge.objects.all()
    serializer_class = EdgeSerializer


class EdgeCreateAPI(CreateAPIView):
    """API for creating Edges"""
    permission_classes = (AllowAny,)
    queryset = Edge.objects.all()
    serializer_class = EdgeSerializer


class EdgeViewAPI(RetrieveAPIView):
    """API for getting a single Edge"""
    permission_classes = (AllowAny,)
    serializer_class = EdgeSerializer
    queryset = Edge.objects.all()
    lookup_field = "uuid"
