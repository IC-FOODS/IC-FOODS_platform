from rest_framework import serializers

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


class ComponentSerializer(serializers.ModelSerializer):
    """Component Serializer"""

    class Meta(object):
        """Meta class for field info"""

        model = Component
        fields = ["uuid", "label", "description"]
        extra_kwargs = {"uuid": {"read_only": True}}


class ConceptSerializer(serializers.ModelSerializer):
    """Concept Serializer"""

    class Meta(object):
        """Meta class for field info"""

        model = Concept
        fields = ["uuid", "label", "iri"]
        extra_kwargs = {"uuid": {"read_only": True}}


class ValueSerializer(serializers.ModelSerializer):
    """Value Serializer"""

    class Meta(object):
        """Meta class for field info"""

        model = Value
        fields = ["uuid", "component", "component_type", "value", "value_type"]
        extra_kwargs = {"uuid": {"read_only": True}}


class ValueAnnotationSerializer(serializers.ModelSerializer):
    """ValueAnnotation Serializer"""

    class Meta(object):
        """Meta class for field info"""

        model = ValueAnnotation
        fields = ["uuid", "value", "annotated_value", "annotation_value"]
        extra_kwargs = {"uuid": {"read_only": True}}


class ResourceSerializer(serializers.ModelSerializer):
    """Resource Serializer"""

    class Meta(object):
        """Meta class for field info"""

        model = Resource
        fields = [
            "uuid",
            "resource_url",
            "resource_type_id",
            "bytes",
            "description",
            "format",
            "identifier",
            "language",
            "publisher",
            "relation",
            "source",
            "subject",
            "label",
            "extent",
        ]
        extra_kwargs = {"uuid": {"read_only": True}}


class RelationSerializer(serializers.ModelSerializer):
    """Relation Serializer"""

    class Meta(object):
        """Meta class for field info"""

        model = Relation
        fields = ["uuid", "label", "definition", "inverse", "iri"]
        extra_kwargs = {"uuid": {"read_only": True}}


class InstanceSerializer(serializers.ModelSerializer):
    """Instance Serializer"""

    class Meta(object):
        """Meta class for field info"""

        model = Instance
        fields = ["uuid", "label", "concept", "item_type"]
        extra_kwargs = {"uuid": {"read_only": True}}


class PropositionSerializer(serializers.ModelSerializer):
    """Proposition Serializer"""

    class Meta(object):
        """Meta class for field info"""

        model = Proposition
        fields = ["uuid", "subject", "predicate", "object", "symetrical"]
        extra_kwargs = {"uuid": {"read_only": True}}


class PropositionDetailsSerializer(serializers.ModelSerializer):
    """Proposition Details Serializer"""

    subject_label = serializers.CharField(source='subject.label', read_only=True)
    object_label = serializers.CharField(source='object.label', read_only=True)
    predicate_label = serializers.CharField(source='predicate.label', read_only=True)

    class Meta(object):
        """Meta class for field info"""

        model = Proposition
        fields = [
            "uuid",
            "subject",
            "subject_label",
            "predicate",
            "predicate_label",
            "object",
            "object_label",
            "symetrical",
        ]
        extra_kwargs = {"uuid": {"read_only": True}}


class MapSerializer(serializers.ModelSerializer):
    """Map Serializer"""

    class Meta(object):
        """Meta class for field info"""

        model = Map
        fields = ["uuid", "root_id", "header", "footer", "stylesheet"]
        extra_kwargs = {"uuid": {"read_only": True}}


class NodeSerializer(serializers.ModelSerializer):
    """Node Serializer"""

    class Meta(object):
        """Meta class for field info"""

        model = Node
        fields = ["uuid", "x_coord", "y_coord", "component", "map", "stylesheet"]
        extra_kwargs = {"uuid": {"read_only": True}}


class EdgeSerializer(serializers.ModelSerializer):
    """Edge Serializer"""

    class Meta(object):
        """Meta class for field info"""

        model = Edge
        fields = ["uuid", "from_node", "to_node", "arrowhead", "map", "stylesheet"]
        extra_kwargs = {"uuid": {"read_only": True}}


class EdgeControlPointSerializer(serializers.ModelSerializer):
    """EdgeControlPoint Serializer"""

    class Meta(object):
        """Meta class for field info"""

        model = EdgeControlPoint
        fields = ["uuid", "edge", "map", "x_coord", "y_coord"]
        extra_kwargs = {"uuid": {"read_only": True}}


class NodeResourceSerializer(serializers.ModelSerializer):
    """NodeResource Serializer"""

    class Meta(object):
        """Meta class for field info"""

        model = NodeResource
        fields = ["uuid", "node", "resource"]
        extra_kwargs = {"uuid": {"read_only": True}}


class StylesheetSerializer(serializers.ModelSerializer):
    """Stylesheet Serializer"""

    class Meta(object):
        """Meta class for field info"""

        model = Stylesheet
        fields = ["uuid", "component", "style"]
        extra_kwargs = {"uuid": {"read_only": True}}
