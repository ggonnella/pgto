#!/usr/bin/env python3
import pronto

def print_tree(term, ontology, level=0, prefix=""):
    children = [child for child in term.subclasses(1, with_self=False)]
    for index, child in enumerate(children):
        if index == len(children) - 1:
            print(f"{prefix}└── {child.id} {child.name}")
            new_prefix = f"{prefix}    "
        else:
            print(f"{prefix}├── {child.id} {child.name}")
            new_prefix = f"{prefix}│   "
        print_tree(child, ontology, level + 1, new_prefix)

ontology_path="group_type.obo"
ontology=pronto.Ontology(ontology_path)

root_terms = [term for term in ontology.values() \
    if isinstance(term, pronto.Term) and \
    "root" in term.namespace]

for root_term in root_terms:
    print(f"{root_term.id} {root_term.name}")
    print_tree(root_term, ontology)
    print("\n")

