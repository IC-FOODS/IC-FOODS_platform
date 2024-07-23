from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.permissions import AllowAny

from icicle_know.models import (
    Component,
    Concept,
    Relation,
    Instance,
    Proposition,
    Value,
    ValueAnnotation,
    Resource,
    Node,
    Edge,
    Map,
    EdgeControlPoint,
    NodeResource,
    Stylesheet,
)
from icicle_know.serializers import (
    ComponentSerializer,
    ConceptSerializer,
    ValueSerializer,
    ValueAnnotationSerializer,
    ResourceSerializer,
    RelationSerializer,
    MapSerializer,
    InstanceSerializer,
    PropositionSerializer,
    PropositionDetailsSerializer,
    NodeSerializer,
    EdgeSerializer,
    EdgeControlPointSerializer,
    NodeResourceSerializer,
    StylesheetSerializer,
)


# Component APIS
class ComponentListAPI(ListAPIView):
    """List API for Components"""
    permission_classes = (AllowAny,)
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer


class ComponentCreateAPI(CreateAPIView):
    """API for creating Components"""
    permission_classes = (AllowAny,)
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer


class ComponentViewAPI(RetrieveAPIView):
    """API for getting a single Component"""
    permission_classes = (AllowAny,)
    serializer_class = ComponentSerializer
    queryset = Component.objects.all()
    lookup_field = "uuid"


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


class PropositionSubjectListAPI(ListAPIView):
    """List API for Propositions by Subject"""
    permission_classes = (AllowAny,)
    serializer_class = PropositionDetailsSerializer

    def get_queryset(self):
        """Get queryset for API"""
        subject_uuid = self.kwargs['subject_uuid']
        return Proposition.objects.filter(subject__uuid=subject_uuid)


class PropositionSubjectPredicateListAPI(ListAPIView):
    """List API for Propositions by Subject and Predicate"""
    permission_classes = (AllowAny,)
    serializer_class = PropositionDetailsSerializer

    def get_queryset(self):
        """Get queryset for API"""
        subject_uuid = self.kwargs['subject_uuid']
        predicate_uuid = self.kwargs['predicate_uuid']

        return Proposition.objects.filter(
            subject__uuid=subject_uuid,
            predicate_uuid=predicate_uuid
        )


class PropositionObjectListAPI(ListAPIView):
    """List API for Propositions by Object"""
    permission_classes = (AllowAny,)
    serializer_class = PropositionDetailsSerializer

    def get_queryset(self):
        """Get queryset for API"""
        object_uuid = self.kwargs['object_uuid']
        return Proposition.objects.filter(object__uuid=object_uuid)


class PropositionObjectPredicateListAPI(ListAPIView):
    """List API for Propositions by Object and Predicate"""
    permission_classes = (AllowAny,)
    serializer_class = PropositionDetailsSerializer

    def get_queryset(self):
        """Get queryset for API"""
        object_uuid = self.kwargs['object_uuid']
        predicate_uuid = self.kwargs['predicate_uuid']

        return Proposition.objects.filter(
            object__uuid=object_uuid,
            predicate__uuid=predicate_uuid
        )


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


# Value APIS
class ValueListAPI(ListAPIView):
    """List API for Values"""
    permission_classes = (AllowAny,)
    queryset = Value.objects.all()
    serializer_class = ValueSerializer


class ValueCreateAPI(CreateAPIView):
    """API for creating Values"""
    permission_classes = (AllowAny,)
    queryset = Value.objects.all()
    serializer_class = ValueSerializer


class ValueViewAPI(RetrieveAPIView):
    """API for getting a single Value"""
    permission_classes = (AllowAny,)
    serializer_class = ValueSerializer
    queryset = Value.objects.all()
    lookup_field = "uuid"


# ValueAnnotation APIS
class ValueAnnotationListAPI(ListAPIView):
    """List API for ValueAnnotations"""
    permission_classes = (AllowAny,)
    queryset = ValueAnnotation.objects.all()
    serializer_class = ValueAnnotationSerializer


class ValueAnnotationCreateAPI(CreateAPIView):
    """API for creating ValueAnnotations"""
    permission_classes = (AllowAny,)
    queryset = ValueAnnotation.objects.all()
    serializer_class = ValueAnnotationSerializer


class ValueAnnotationViewAPI(RetrieveAPIView):
    """API for getting a single ValueAnnotation"""
    permission_classes = (AllowAny,)
    serializer_class = ValueAnnotationSerializer
    queryset = ValueAnnotation.objects.all()
    lookup_field = "uuid"


# Resource APIS
class ResourceListAPI(ListAPIView):
    """List API for Resources"""
    permission_classes = (AllowAny,)
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class ResourceCreateAPI(CreateAPIView):
    """API for creating Resources"""
    permission_classes = (AllowAny,)
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class ResourceViewAPI(RetrieveAPIView):
    """API for getting a single Resource"""
    permission_classes = (AllowAny,)
    serializer_class = ResourceSerializer
    queryset = Resource.objects.all()
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


# Map APIS
class MapListAPI(ListAPIView):
    """List API for Maps"""
    permission_classes = (AllowAny,)
    queryset = Map.objects.all()
    serializer_class = MapSerializer


class MapCreateAPI(CreateAPIView):
    """API for creating Maps"""
    permission_classes = (AllowAny,)
    queryset = Map.objects.all()
    serializer_class = MapSerializer


class MapViewAPI(RetrieveAPIView):
    """API for getting a single Map"""
    permission_classes = (AllowAny,)
    serializer_class = MapSerializer
    queryset = Map.objects.all()
    lookup_field = "uuid"


# EdgeControlPoint APIS
class EdgeControlPointListAPI(ListAPIView):
    """List API for EdgeControlPoints"""
    permission_classes = (AllowAny,)
    queryset = EdgeControlPoint.objects.all()
    serializer_class = EdgeControlPointSerializer


class EdgeControlPointCreateAPI(CreateAPIView):
    """API for creating EdgeControlPoints"""
    permission_classes = (AllowAny,)
    queryset = EdgeControlPoint.objects.all()
    serializer_class = EdgeControlPointSerializer


class EdgeControlPointViewAPI(RetrieveAPIView):
    """API for getting a single EdgeControlPoint"""
    permission_classes = (AllowAny,)
    serializer_class = EdgeControlPointSerializer
    queryset = EdgeControlPoint.objects.all()
    lookup_field = "uuid"


# NodeResource APIS
class NodeResourceListAPI(ListAPIView):
    """List API for NodeResources"""
    permission_classes = (AllowAny,)
    queryset = NodeResource.objects.all()
    serializer_class = NodeResourceSerializer


class NodeResourceCreateAPI(CreateAPIView):
    """API for creating NodeResources"""
    permission_classes = (AllowAny,)
    queryset = NodeResource.objects.all()
    serializer_class = NodeResourceSerializer


class NodeResourceViewAPI(RetrieveAPIView):
    """API for getting a single NodeResource"""
    permission_classes = (AllowAny,)
    serializer_class = NodeResourceSerializer
    queryset = NodeResource.objects.all()
    lookup_field = "uuid"


# Stylesheet APIS
class StylesheetListAPI(ListAPIView):
    """List API for Stylesheets"""
    permission_classes = (AllowAny,)
    queryset = Stylesheet.objects.all()
    serializer_class = StylesheetSerializer


class StylesheetCreateAPI(CreateAPIView):
    """API for creating Stylesheets"""
    permission_classes = (AllowAny,)
    queryset = Stylesheet.objects.all()
    serializer_class = StylesheetSerializer


class StylesheetViewAPI(RetrieveAPIView):
    """API for getting a single Stylesheet"""
    permission_classes = (AllowAny,)
    serializer_class = StylesheetSerializer
    queryset = Stylesheet.objects.all()
    lookup_field = "uuid"
