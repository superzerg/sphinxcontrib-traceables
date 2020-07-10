import pytest
import os
from xml.etree import ElementTree


@pytest.mark.sphinx(buildername="xml", testroot="list")
def test_list(app):
    app.build()

    # Verify that basic list has 2 list item nodes.
    tree = ElementTree.parse(os.path.join(app.outdir, "list_basic.xml"))
    assert len(tree.findall(".//list_item")) == 2

    # Verify that filtered list has 1 list item node.
    tree = ElementTree.parse(os.path.join(app.outdir, "list_filter.xml"))
    assert len(tree.findall(".//list_item")) == 1
