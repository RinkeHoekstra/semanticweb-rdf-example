from rdflib import Graph
from RDFClosure import DeductiveClosure, RDFS_Semantics
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run RDFS inferencing over a turtle file")
    parser.add_argument('path', type=str, help="The path to the Turtle file to load")

    args = parser.parse_args()

    g = Graph()
    g.load(args.path, format='turtle')

    DeductiveClosure(RDFS_Semantics, rdfs_closure = True, axiomatic_triples = False, datatype_axioms = False).expand(g)

    print g.serialize(format='turtle')
