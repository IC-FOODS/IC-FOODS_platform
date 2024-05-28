from django.db import models

from icicle_base.models import UUIDBaseModel


class Component(UUIDBaseModel):
    """
    Component Model
    """
    title = models.CharField(max_length=128,blank=False,)
    description = models.TextField()


class Concept(UUIDBaseModel):
    """
    Concept Model
    """
    title = models.CharField(max_length=128,blank=False,)
    iri = models.CharField(max_length=256,blank=False,)


class Relation(UUIDBaseModel):
    """
    Relation Model
    """
    title = models.CharField(max_length=128,blank=False,)
    definition = models.TextField()
    inverse = models.ForeignKey("Relation",on_delete=models.CASCADE,null=True,)
    iri = models.CharField(max_length=256,blank=False,)


class Instance(UUIDBaseModel):
    """
    Instance Model
    """
    title = models.CharField(max_length=128,blank=False,)
    concept = models.ForeignKey("Concept",on_delete=models.CASCADE,null=True,)
    item_type = models.CharField(max_length=128,blank=False,)


class Proposition(UUIDBaseModel):
    """
    Proposition Model
    """
    subject = models.ForeignKey("Instance",on_delete=models.CASCADE,null=True, related_name="subject_prop")
    predicate = models.ForeignKey("Relation",on_delete=models.CASCADE,null=True,)
    object = models.ForeignKey("Instance",on_delete=models.CASCADE,null=True, related_name="object_prop")
    symetrical = models.BooleanField(default=False)


class Value(UUIDBaseModel):
    """
    Value Model
    """
    component = models.ForeignKey("Component",on_delete=models.CASCADE,null=True,)
    component_type = models.CharField(max_length=128,blank=False,)
    value = models.CharField(max_length=128,blank=False,)
    value_type = models.CharField(max_length=128,blank=False,)


class ValueAnnotation(UUIDBaseModel):
    """
    ValueAnnotation Model
    """
    value = models.ForeignKey("Value",on_delete=models.CASCADE,null=True,)
    annotated_value = models.CharField(max_length=128,blank=False,)
    annotation_value = models.CharField(max_length=128,blank=False,)


class Resource(UUIDBaseModel):
    """
    Resource Model
    """
    resource_url = models.CharField(max_length=128,blank=False,)
    resource_type_id = models.CharField(max_length=128,blank=False,)
    bytes = models.IntegerField(null=False)
    description = models.TextField()
    format = models.CharField(max_length=128,blank=False,)
    identifier = models.CharField(max_length=128,blank=False,)
    language = models.CharField(max_length=2,blank=False,)
    publisher = models.CharField(max_length=128,blank=False,)
    relation = models.CharField(max_length=128,blank=False,)
    source = models.CharField(max_length=128,blank=False,)
    subject = models.CharField(max_length=128,blank=False,)
    title = models.CharField(max_length=128,blank=False,)
    extent = models.CharField(max_length=128,blank=False,)


class Map(UUIDBaseModel):
    """
    Map Model
    """
    root_id = models.CharField(max_length=128,blank=False,)
    header = models.TextField()
    footer = models.TextField()
    stylesheet = models.ForeignKey("Stylesheet",on_delete=models.CASCADE,null=True,)


class Node(UUIDBaseModel):
    """
    Node Model
    """
    component = models.ForeignKey("Component",on_delete=models.CASCADE,null=True,)
    map = models.ForeignKey("Map",on_delete=models.CASCADE,null=True,)
    x_coord = models.IntegerField(null=False)
    y_coord = models.IntegerField(null=False)
    stylesheet = models.ForeignKey("Stylesheet",on_delete=models.CASCADE,null=True,)


class Edge(UUIDBaseModel):
    """
    Edge Model
    """
    map = models.ForeignKey("Map",on_delete=models.CASCADE,null=True,)
    from_node = models.ForeignKey("Node",on_delete=models.CASCADE,null=True, related_name="from_edge")
    to_node = models.ForeignKey("Node",on_delete=models.CASCADE,null=True, related_name="to_edge")
    arrowhead = models.CharField(max_length=64,blank=False,)
    stylesheet = models.ForeignKey("Stylesheet",on_delete=models.CASCADE,null=True,)


class EdgeControlPoint(UUIDBaseModel):
    """
    EdgeControlPoint Model
    """
    edge = models.ForeignKey("Edge",on_delete=models.CASCADE,null=True,)
    map = models.ForeignKey("Map",on_delete=models.CASCADE,null=True,)
    x_coord = models.IntegerField(null=False)
    y_coord = models.IntegerField(null=False)


class Stylesheet(UUIDBaseModel):
    """
    Stylesheet Model
    """
    component = models.ForeignKey("Component",on_delete=models.CASCADE,null=True,)
    style = models.JSONField()