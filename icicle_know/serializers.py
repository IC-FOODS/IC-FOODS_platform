from rest_framework import serializers

from icicle_know.models import (
    Concept,
    Relation,
    Instance,
    Proposition,
    Node,
    Edge,
)


class ConceptSerializer(serializers.ModelSerializer):
    """Concept Serializer"""

    class Meta(object):
        """Meta class for field info"""

        model = Concept
        fields = ["uuid", "title", "iri"]
        extra_kwargs = {"uuid": {"read_only": True}}


class RelationSerializer(serializers.ModelSerializer):
    """Relation Serializer"""

    class Meta(object):
        """Meta class for field info"""

        model = Relation
        fields = ["uuid", "title", "definition", "inverse", "iri"]
        extra_kwargs = {"uuid": {"read_only": True}}


class InstanceSerializer(serializers.ModelSerializer):
    """Instance Serializer"""

    class Meta(object):
        """Meta class for field info"""

        model = Instance
        fields = ["uuid", "title", "concept", "item_type"]
        extra_kwargs = {"uuid": {"read_only": True}}


class PropositionSerializer(serializers.ModelSerializer):
    """Proposition Serializer"""

    class Meta(object):
        """Meta class for field info"""

        model = Proposition
        fields = ["uuid", "subject", "predicate", "object", "symetrical"]
        extra_kwargs = {"uuid": {"read_only": True}}


class NodeSerializer(serializers.ModelSerializer):
    """Node Serializer"""

    class Meta(object):
        """Meta class for field info"""

        model = Node
        fields = ["uuid", "x_coord", "y_coord"]
        extra_kwargs = {"uuid": {"read_only": True}}


class EdgeSerializer(serializers.ModelSerializer):
    """Edge Serializer"""

    class Meta(object):
        """Meta class for field info"""

        model = Edge
        fields = ["uuid", "from_node", "to_node", "arrowhead"]
        extra_kwargs = {"uuid": {"read_only": True}}
