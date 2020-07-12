import pytest
from sphinxcontrib.traceables.infrastructure import TraceablesStorage


@pytest.mark.sphinx(buildername="xml", testroot="basics")
def test_infrastructure(app):
    app.build()
    storage = TraceablesStorage(app.env)

    # Verify exception on invalid relationship name.
    pytest.raises(ValueError, storage.get_relationship_direction, "invalid")
    pytest.raises(ValueError, storage.get_relationship_opposite, "invalid")

    # Verify Traceable.__str__() doesn't fail.
    for traceable in storage.traceables_set:
        ignored_output = str(traceable)
