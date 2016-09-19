# RDF Example from the Semantic Web course

This repository contains two Turtle files:

* `example-from-slides.ttl` which contains the RDF for the european country example given in class
* `example-live.ttl` contains the RDF we produced in class (about our forest and our house)

The `infer.py` file is a command-line utility for running RDF Schema inferencing over a Turtle file:

`python infer.py FILENAME.ttl`

The `example.ipynb` is a Jupyter notebook that I used in class.

### How can I use it?

To make all of this work, you need to install the following:

* The usual `pip install rdflib` (you should have that already)
* The OWL-RL reasoning engine by Ivan Herman: <https://github.com/RDFLib/OWL-RL/archive/master.zip>
  * unzip it, and then from the directory you created, run `python setup.py install`
* If you want to use the notebook, you need to `pip install jupyter`, then run it using `jupyter notebook` from the directory that contains the `example.ipynb`. For more information about Jupyter, have a look at <http://jupyter.org>.
