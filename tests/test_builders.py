import pytest


@pytest.mark.sphinx(buildername="html", testroot="matrix")
def test_builder_html(app):
    '''Verify that HTML builder doesn't fail'''
    app.build()


@pytest.mark.sphinx(buildername="latex", testroot="matrix")
def test_latex_builder(app):
    '''Verify that Latex builder doesn't fail'''
    app.build()
