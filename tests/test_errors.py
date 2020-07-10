import pytest


@pytest.mark.sphinx(buildername="xml", testroot="errors")
def test_basics(app, status, warning):
    app.build()
#    tree = ElementTree.parse(app.outdir / "index.xml")
#    pretty_print_xml(tree.getroot())

    # Verify that a warning is emitted for doubly defined traceable tag.
    assert (warning.getvalue().find(
        "WARNING: More than one traceable with tag 'SAGITTA' found!") > 0)

    # Verify that a warning is emitted for doubly defined traceable tag.
    assert (warning.getvalue().find(
        "WARNING: Traceable attribute has invalid syntax") > 0)
