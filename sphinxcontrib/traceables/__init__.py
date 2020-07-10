
from .infrastructure import ProcessorManager, setup as infrastructure_setup
from .display import TraceableDisplayProcessor, setup as display_setup
from .traceables import RelationshipsProcessor, XrefProcessor, setup as traceables_setup
from .list import ListProcessor, setup as list_setup
from .matrix import MatrixProcessor, setup as matrix_setup
from .graph import GraphProcessor, setup as graph_setup


# ==========================================================================
# Setup and register extension

def setup(app):
    # Allow extension parts to set themselves up.
    infrastructure_setup(app)
    display_setup(app)
    traceables_setup(app)
    list_setup(app)
    matrix_setup(app)
    graph_setup(app)

    # Register business logic of extension parts. This is done explicitly
    # here to ensure correct ordering during processing.
    ProcessorManager.register_processor_classes([
        RelationshipsProcessor,
        TraceableDisplayProcessor,
        XrefProcessor,
        ListProcessor,
        MatrixProcessor,
        GraphProcessor,
    ])

    return {"version": "0.0"}
