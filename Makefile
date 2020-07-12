# You can set these variables from the command line, and also
# from the environment.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build

.PHONY: all main_doc consellations_doc requirements_doc test_basics_doc test_graph_doc test_list_doc test_matrix_doc

all: main_doc consellations_doc requirements_doc test_basics_doc test_graph_doc test_list_doc test_matrix_doc

# $(O) is meant as a shortcut for $(SPHINXOPTS).
main_doc: docs/conf.py docs/gettingstarted.txt docs/index.txt docs/internals.txt docs/license.txt docs/logicarch.txt docs/usage.txt
	@$(SPHINXBUILD) "./docs" "./docs/_build" $(SPHINXOPTS) $(O)
	touch docs/_build/.nojekyll
	
consellations_doc: examples/constellations/conf.py examples/constellations/graph.txt examples/constellations/hercules.txt examples/constellations/index.txt examples/constellations/lacaille.txt examples/constellations/matrix.txt examples/constellations/perseus.txt
	@$(SPHINXBUILD) "./examples/constellations" "./docs/_build/constellations" $(SPHINXOPTS) $(O)
	
requirements_doc: examples/requirements/conf.py examples/requirements/index.txt examples/requirements/strs.txt examples/requirements/syrs.txt examples/requirements/verif.txt
	@$(SPHINXBUILD) "./examples/requirements" "./docs/_build/requirements" $(SPHINXOPTS) $(O)

test_graph_doc: tests/data/test-graph/conf.py tests/data/test-graph/index.txt
	@$(SPHINXBUILD) "./tests/data/test-graph" "./docs/_build/test-graph" $(SPHINXOPTS) $(O)
	
test_list_doc: tests/data/test-list/conf.py tests/data/test-list/index.txt tests/data/test-list/list_basic.txt tests/data/test-list/list_filter.txt
	@$(SPHINXBUILD) "./tests/data/test-list" "./docs/_build/test-list" $(SPHINXOPTS) $(O)
	
test_matrix_doc: tests/data/test-matrix/conf.py tests/data/test-matrix/index.txt tests/data/test-matrix/matrix_columns.txt tests/data/test-matrix/matrix_default.txt tests/data/test-matrix/matrix_list.txt tests/data/test-matrix/matrix_table.txt
	@$(SPHINXBUILD) "./tests/data/test-matrix" "./docs/_build/test-matrix" $(SPHINXOPTS) $(O)
