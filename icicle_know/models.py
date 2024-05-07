from django.db import models

from icicle_base.models import UUIDBaseModel


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


class Node(UUIDBaseModel):
    """
    Node Model
    """
    # component = models.ForeignKey("Map",on_delete=models.CASCADE,null=True,)
    # map = models.ForeignKey("Map",on_delete=models.CASCADE,null=True,)
    x_coord = models.IntegerField(null=False)
    y_coord = models.IntegerField(null=False)
    # stylesheet = models.ForeignKey("Stylesheet",on_delete=models.CASCADE,null=True,)


class Edge(UUIDBaseModel):
    """
    Edge Model
    """
    # map = models.ForeignKey("Map",on_delete=models.CASCADE,null=True,)
    from_node = models.ForeignKey("Node",on_delete=models.CASCADE,null=True, related_name="from_edge")
    to_node = models.ForeignKey("Node",on_delete=models.CASCADE,null=True, related_name="to_edge")
    arrowhead = models.CharField(max_length=64,blank=False,)
    # stylesheet = models.ForeignKey("Stylesheet",on_delete=models.CASCADE,null=True,)
