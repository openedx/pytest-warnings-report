# -*- coding: utf-8 -*-
""" Tests for the warnings report. """
import os


def test_warnings_written(testdir):
    """Make sure that pytest accepts our fixture."""

    # create a temporary pytest test module
    testdir.makepyfile("""
        import logging
        def test_sth():
            logging.warning('A test warning')
            assert True
    """)
    testdir.runpytest('--json-report')
    for f in os.listdir(testdir.tmpdir):
        print(f)
    with open(testdir.tmpdir / '.report.json') as content:
        print(content.read())
    assert (testdir.tmpdir / 'test_root/log/pytest_warnings.json').exists()
