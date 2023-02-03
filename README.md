# PGTO: Prokaryotic Group Types Ontology

In some bioinformatics applications, group of prokaryotic
organisms must be defined exactly.
For example, one could describe which expectations one has, about the content
of a genome in given groups of organisms.

These groups belong to different types, e.g. a bacterial phylum is a taxonomic group
and all anaerobic bacteria are a group based on the oxygen requirement as a
defining criterion.
The Prokaryotic Group Types Ontology gives a framework for the definition of
such groups, by defining possible group types and classifying them in categories.

## Ontology files

The ontology is defined using the OBO format and consists of a single file,
(``group\_types.obo``).

## Structure and contents

The goal of the PGTO ontology are group type definitions.
These are summarized in categories, which are children of the root node
``group type categories``.

The categories include:
- habitat requirement type
- phenotype group type
- location group type
- phylogenetic group type
- derived group type.

Of these, the first 4 group types categories are for types of simple groups,
which are not dependant on the definition of other groups, while the
last is for derived groups, whose definition is the combination or negation
of other group definitions.

Besides the group categories and group type definitions,
the ontology contains metadata terms, which are included in the
namespace \textit{metadata}.
These contain the following definitions:
- group combination and inversion expression (and their ancestors),
  which are used in the definitions of derived groups
- external resources-related terms, including broad definitions (external resource)
down to very specific terms (taxonomy database)
- optional attributes, useful for some definitions.

Furthemore, some relationships are defined:
- ``defined by``, used in the derived group definition, to connect them to
  logical expressions
- relationship expressing the requirement of external resources
- relationship expressing the existance of optional attributes.

## Defining a new group type

When, in an application, a group of prokaryotic organisms is defined,
first all existing group types under the
``group\_type`` namespace must be considered.

If the definition of the group does not logically belong to
any of the defined group types, then a new group type can be defined
and added to the ontology.

In this case, the best fitting category must be chosen for the group
type, among those in the namespace ``group types category``.
If no category fits, then one can be defined and added to the ontology
(this should be rarely the case).

## Acknowledgements

This ontology has been created in context of the
DFG project GO 3192/1-1 “Automated
characterization of microbial genomes and metagenomes by collection and
verification of association rules”. The funders had no role in
study design, data collection
and analysis.
