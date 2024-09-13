from django.db import models

from icicle_base.models import UUIDBaseModel


class Component(UUIDBaseModel):
    """
    Component Model
    """
    label = models.CharField(max_length=255,blank=False,)
    description = models.TextField()


class Concept(UUIDBaseModel):
    """
    Concept Model
    """
    label = models.CharField(max_length=255,blank=False,)
    iri = models.CharField(max_length=256,blank=False,)


class Relation(UUIDBaseModel):
    """
    Relation Model
    """
    label = models.CharField(max_length=255,blank=False,)
    definition = models.TextField()
    inverse = models.ForeignKey("Relation",on_delete=models.CASCADE,null=True,)
    iri = models.CharField(max_length=256,blank=False,)


class Instance(UUIDBaseModel):
    """
    Instance Model
    """
    label = models.CharField(max_length=255,blank=False,)
    concept = models.ForeignKey("Concept",on_delete=models.CASCADE,null=True,)
    item_type = models.CharField(max_length=255,blank=False,)


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
    component_type = models.CharField(max_length=255,blank=False,)
    value = models.CharField(max_length=255,blank=False,)
    value_type = models.CharField(max_length=255,blank=False,)


class ValueAnnotation(UUIDBaseModel):
    """
    ValueAnnotation Model
    """
    value = models.ForeignKey("Value",on_delete=models.CASCADE,null=True,)
    annotated_value = models.CharField(max_length=255,blank=False,)
    annotation_value = models.CharField(max_length=255,blank=False,)


class Resource(UUIDBaseModel):
    """
    Resource Model
    """
    resource_url = models.CharField(max_length=255,blank=False,)
    resource_type_id = models.CharField(max_length=255,blank=False,)
    bytes = models.IntegerField(null=False)
    description = models.TextField()
    format = models.CharField(max_length=255,blank=False,)
    identifier = models.CharField(max_length=255,blank=False,)
    language = models.CharField(max_length=2,blank=False,)
    publisher = models.CharField(max_length=255,blank=False,)
    relation = models.CharField(max_length=255,blank=False,)
    source = models.CharField(max_length=255,blank=False,)
    subject = models.CharField(max_length=255,blank=False,)
    label = models.CharField(max_length=255,blank=False,)
    extent = models.CharField(max_length=255,blank=False,)


class Map(UUIDBaseModel):
    """
    Map Model
    """
    root_id = models.CharField(max_length=255,blank=False,)
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


class NodeResource(UUIDBaseModel):
    """
    NodeResource Model
    """
    node = models.ForeignKey("Node",on_delete=models.CASCADE,null=True,)
    resource = models.ForeignKey("Resource",on_delete=models.CASCADE,null=True,)


class Stylesheet(UUIDBaseModel):
    """
    Stylesheet Model
    """
    component = models.ForeignKey("Component",on_delete=models.CASCADE,null=True,)
    style = models.JSONField()


class KbD5C47Fc464AssertedStatements(models.Model):
    subject = models.TextField()
    predicate = models.TextField()
    object = models.TextField()
    context = models.TextField()
    termcomb = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kb_d5c47fc464_asserted_statements'
        unique_together = (('subject', 'predicate', 'object', 'context'),)


class KbD5C47Fc464LiteralStatements(models.Model):
    subject = models.TextField()
    predicate = models.TextField()
    object = models.TextField(blank=True, null=True)
    context = models.TextField()
    termcomb = models.IntegerField()
    objlanguage = models.CharField(max_length=255, blank=True, null=True)
    objdatatype = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kb_d5c47fc464_literal_statements'
        unique_together = (('subject', 'predicate', 'object', 'objlanguage', 'context'),)


class KbD5C47Fc464NamespaceBinds(models.Model):
    prefix = models.CharField(primary_key=True, max_length=20)
    uri = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kb_d5c47fc464_namespace_binds'


class KbD5C47Fc464QuotedStatements(models.Model):
    subject = models.TextField()
    predicate = models.TextField()
    object = models.TextField(blank=True, null=True)
    context = models.TextField()
    termcomb = models.IntegerField()
    objlanguage = models.CharField(max_length=255, blank=True, null=True)
    objdatatype = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kb_d5c47fc464_quoted_statements'
        unique_together = (('subject', 'predicate', 'object', 'objlanguage', 'context'),)


class KbD5C47Fc464TypeStatements(models.Model):
    member = models.TextField()
    klass = models.TextField()
    context = models.TextField()
    termcomb = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kb_d5c47fc464_type_statements'
        unique_together = (('member', 'klass', 'context'),)
