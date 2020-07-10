import pytest
from nose.tools import assert_raises
from sphinxcontrib.traceables.infrastructure import TraceablesStorage


@pytest.mark.sphinx(buildername="xml", testroot="basics")
def test_infrastructure(app):
    app.build()
    storage = TraceablesStorage(app.env)

    # Verify exception on invalid relationship name.
    assert_raises(ValueError, storage.get_relationship_direction, "invalid")
    assert_raises(ValueError, storage.get_relationship_opposite, "invalid")

    # Verify Traceable.__str__() doesn't fail.
    for traceable in storage.traceables_set:
        ignored_output = str(traceable)
