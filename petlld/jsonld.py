"""
Apply a JSON-LD context to a Petl table to transform to an RDFLib Graph 
for futher processing or serialization as RDF.
"""

# standard library dependencies
import json

# internal dependencies
from petl.util.base import Table, dicts as _dicts
from petl.io.json import _writejson

from rdflib import ConjunctiveGraph
from rdflib_jsonld.parser import to_rdf

def add_context(data, context):
    return {
        '@context': context,
        '@graph': data
    }

def tojsonld(table, context, source=None, prefix=None, suffix=None, *args, **kwargs):
    """
    Add the JSON-LD context to the table.

    From petl:
    Note that this is currently not streaming, all data is loaded into memory
    before being written to the file.
    """
    obj = list(_dicts(table))
    data = add_context(obj, context)
    #return json.dumps(data, indent=2)
    _writejson(source, data, prefix, suffix, *args, **kwargs)

Table.tojsonld = tojsonld

def graph_from_ld(data):
    g = ConjunctiveGraph()
    out = to_rdf(data, g)
    return g

def tograph(table, context, *args, **kwargs):
    """
    Return an RDFLib Graph of the table using the context.
    """
    obj = list(_dicts(table))
    data = add_context(obj, context)
    return graph_from_ld(data)

Table.tograph = tograph