import pytest
from sphinxcontrib.traceables.infrastructure import TraceablesStorage
from sphinxcontrib.traceables.matrix import TraceableMatrix


def eq_(a, b, msg=None):
    assert a == b, "%r != %r" % (a, b)


@pytest.mark.sphinx(buildername="xml", testroot="traceable_matrix")
def test_traceable_matrix(app):
    app.build()
    storage = TraceablesStorage(app.env)

    # Construct a traceable matrix.
    forward = "children"
    backward = storage.get_relationship_opposite(forward)
    matrix = TraceableMatrix(forward, backward)
    for traceable in storage.traceables_set:
        relatives = traceable.relationships.get(forward, ())
        for relative in relatives:
            matrix.add_traceable_pair(traceable, relative)

    # Verify correct primaries and secondaries.
    eq_([t.tag for t in matrix.primaries], [u"CEPHEUS", u"SAGITTA"])
    eq_([t.tag for t in matrix.secondaries], [u"AQUILA", u"AURIGA", u"LYRA"])

    # Verify correct splitting of traceable matrix.
    submatrices = matrix.split(2)
    eq_(len(submatrices), 2)
    verify_submatrices(matrix, submatrices)

    submatrices = matrix.split(2, 1)
    eq_(len(submatrices), 4)
    verify_submatrices(matrix, submatrices)

    submatrices = matrix.split(1)
    eq_(len(submatrices), 3)
    verify_submatrices(matrix, submatrices)

    submatrices = matrix.split(None, 1)
    eq_(len(submatrices), 2)
    verify_submatrices(matrix, submatrices)


def verify_submatrices(matrix, submatrices):
    for submatrix in submatrices:
        for primary in submatrix.primaries:
            boolean_row = submatrix.get_boolean_row(primary)
            for (is_related, secondary) in zip(boolean_row,
                                               submatrix.secondaries):
                eq_(is_related, secondary in matrix.get_relatives(primary))


def test_traceable_matrix_calculate_ranges():
    matrix = TraceableMatrix("forward", "backward")
    eq_(matrix.calculate_ranges(5, None), [(0, 5)])
    eq_(matrix.calculate_ranges(5, 0), [(0, 5)])
    eq_(matrix.calculate_ranges(5, 1), [(0, 1), (1, 2), (2, 3), (3, 4),
                                        (4, 5)])
    eq_(matrix.calculate_ranges(5, 2), [(0, 2), (2, 4), (4, 5)])
    eq_(matrix.calculate_ranges(5, 3), [(0, 3), (3, 5)])
    eq_(matrix.calculate_ranges(5, 4), [(0, 4), (4, 5)])
    eq_(matrix.calculate_ranges(5, 5), [(0, 5)])
    eq_(matrix.calculate_ranges(5, 6), [(0, 5)])
