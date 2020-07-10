
import os
from sphinx_testing.util import with_app
from xml.etree import ElementTree
from xml.dom.minidom import parseString


# =============================================================================
# Utility functions

def srcdir(name):
    test_root = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(test_root, "data", name)


def pretty_print_xml(node):
    minidom_xml = parseString(ElementTree.tostring(node))
    output = minidom_xml.toprettyxml(indent="  ")
    lines = [line for line in output.splitlines() if line.strip()]
    print("\n".join(lines))


def with_app(*args, **kwargs):
    kwargs = kwargs.copy()

    # Expand test data directory.
    if "srcdir" in kwargs:
        kwargs["srcdir"] = srcdir(kwargs["srcdir"])

    # By default use a fresh build environment.
    if "freshenv" not in kwargs:
        kwargs["freshenv"] = True

    return with_app(*args, **kwargs)
