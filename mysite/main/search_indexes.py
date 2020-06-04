# import datetime
from haystack import indexes
from .models import Generic

# Check out this page for querying the whoosh_index!
# https://stackoverflow.com/questions/2395675/whoosh-index-viewer

# Elasticsearch installation and running (version 2.4.6 required as later version not supported by haystack)
# nb: requires jdk v8
# https://www.elastic.co/guide/en/elasticsearch/reference/7.1/targz.html


class GenericIndex(indexes.SearchIndex, indexes.Indexable):
    
    text = indexes.CharField(document=True, use_template=True)
    string1_auto = indexes.NgramField(model_attr="string1")
    string2_auto = indexes.NgramField(model_attr="string2")
    string3_auto = indexes.NgramField(model_attr="string3")
    string4_auto = indexes.NgramField(model_attr="string4")
    string5_auto = indexes.NgramField(model_attr="string5")
    string6_auto = indexes.NgramField(model_attr="string6")
    string7_auto = indexes.NgramField(model_attr="string7")
    string8_auto = indexes.NgramField(model_attr="string8")
    string9_auto = indexes.NgramField(model_attr="string9")
    string10_auto = indexes.NgramField(model_attr="string10") 
    date1_auto = indexes.DateTimeField(model_attr="date1", null=True)
    date2_auto = indexes.DateTimeField(model_attr="date2", null=True)
    date3_auto = indexes.DateTimeField(model_attr="date3", null=True)
    date4_auto = indexes.DateTimeField(model_attr="date4", null=True)
    date5_auto = indexes.DateTimeField(model_attr="date5", null=True)
    float1_auto = indexes.FloatField(model_attr="float1", null=True)
    float2_auto = indexes.FloatField(model_attr="float2", null=True)
    float3_auto = indexes.FloatField(model_attr="float3", null=True)
    float4_auto = indexes.FloatField(model_attr="float4", null=True)
    float5_auto = indexes.FloatField(model_attr="float5", null=True)
    int1_auto = indexes.IntegerField(model_attr="int1", null=True)
    int2_auto = indexes.IntegerField(model_attr="int2", null=True)
    int3_auto = indexes.IntegerField(model_attr="int3", null=True)
    int4_auto = indexes.IntegerField(model_attr="int4", null=True)
    int5_auto = indexes.IntegerField(model_attr="int5", null=True)
    status_auto = indexes.NgramField(model_attr="status")

    def get_model(self):
        return Generic

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        # return self.get_model().objects.filter(hack_published__lte=datetime.datetime.now())
        return self.get_model().objects.all()
