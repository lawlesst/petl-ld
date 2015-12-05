from __future__ import print_function

import petl as etl
import petlld
import json
import csv

from rdflib import Graph, URIRef

fname = '/tmp/example.csv'

# set up a CSV file to demonstrate with
table1 = [['uri', 'name'],
          ['n1', "Smith, Bob"],
          ['n2', "Jones, Sally"],
          ['n3', "Adams, Bill"]]

ctx = {
    "@base": "http://example.org/people/",
    "a": "@type",
    "uri": "@id",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "name": "rdfs:label"
}

tmpfile = '/tmp/jld.json'

def test_tojsonld():
    """
    Test serializing as JSON LD.
    """
    #serialize as jsonld
    table2 = etl.addfield(table1, 'a', 'foaf:Person')
    table2.tojsonld(ctx, source=tmpfile)

    with open(tmpfile, 'rb') as inf:
        data = json.load(inf)
        #Check context
        assert data['@context']['foaf'].find('foaf') > -1
        assert data['@graph'][0].get('name') is not None

def test_tograph():
    """
    Test converting a table to a Graph.
    """
    table2 = etl.addfield(table1, 'a', 'foaf:Person')
    g = table2.tograph(ctx)
    nt = g.serialize(format='nt')
    assert '<http://example.org/people/n2>' in nt
    assert '<http://xmlns.com/foaf/0.1/Person>' in nt

    #read back in as string
    ng = Graph().parse(data=nt, format='nt')
