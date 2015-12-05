import petl as etl
import petlld

# set up a petl table  to demonstrate
table1 = [['uri', 'name'],
          ['n1', "Smith, Bob"],
          ['n2', "Jones, Sally"],
          ['n3', "Adams, Bill"]]

# use petl utilities to add a column with our data type - foaf:Person
table2 = etl.addfield(table1, 'a', 'foaf:Person')

# a JSON-LD context for our data
ctx = {
    "@base": "http://example.org/people/",
    "a": "@type",
    "uri": "@id",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "name": "rdfs:label"
}

# serialize the data as JSON-LD
table2.tojsonld(ctx, indent=2)

graph = table2.tograph(ctx)

print
print '-' * 10
print

print graph.serialize(format='turtle')
