
import os
from xml.etree import ElementTree
import pytest


@pytest.mark.sphinx(buildername="xml", testroot="matrix")
def test_matrix_structure(app):
    '''Verify generated XML structure for different matrix formats'''
    app.build()

    # Verify matrix with list format.
    tree = ElementTree.parse(os.path.join(app.outdir, "matrix_list.xml"))
#    print pretty_print_xml(tree.getroot())
    # Verify that the correct number of list items were generated.
    assert len(tree.findall(".//list_item")) == 11

    # Verify matrix with columns format.
    tree = ElementTree.parse(os.path.join(app.outdir, "matrix_columns.xml"))
#    pretty_print_xml(tree.getroot())
    # Verify that the correct number of rows and entries were generated.
    rows = tree.findall(".//tbody/row")
    assert len(rows) == 3
    assert len(rows[0].findall("./entry")) == 2

    # Verify matrix with table format.
    tree = ElementTree.parse(os.path.join(app.outdir, "matrix_table.xml"))
#    pretty_print_xml(tree.getroot())
    # Verify that the correct number of rows and entries were generated.
    rows = tree.findall(".//tbody/row")
    assert len(rows) == 3
    assert len(rows[0].findall("./entry")) == 3
