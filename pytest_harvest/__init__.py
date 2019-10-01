from pytest_harvest.common import get_fixture_value, HARVEST_PREFIX
from pytest_harvest.fixture_cache import saved_fixture
from pytest_harvest.results_bags import create_results_bag_fixture, ResultsBag
from pytest_harvest.results_session import get_session_synthesis_dct, PYTEST_OBJ_NAME, filter_session_items,\
    get_all_pytest_param_names, get_all_pytest_fixture_names, get_pytest_status, get_pytest_params, \
    get_pytest_param_names, is_pytest_incomplete, pytest_item_matches_filter

try:
    # -- Distribution mode --
    # import from _version.py generated by setuptools_scm during release
    from ._version import version as __version__
except ImportError:
    # -- Source mode --
    # use setuptools_scm to get the current version from src using git
    from setuptools_scm import get_version as _gv
    from os import path as _path
    __version__ = _gv(_path.join(_path.dirname(__file__), _path.pardir))

__all__ = [
    '__version__',

    # submodules
    'fixture_cache', 'results_bags', 'results_session',

    # symbols imported above
    'get_fixture_value', 'HARVEST_PREFIX',
    'saved_fixture',
    'create_results_bag_fixture', 'ResultsBag',
    # session related
    'get_session_synthesis_dct', 'PYTEST_OBJ_NAME', 'get_all_pytest_param_names', 'get_all_pytest_fixture_names',
    'filter_session_items',
    # item related
    'get_pytest_status', 'get_pytest_params', 'get_pytest_param_names', 'is_pytest_incomplete',
    'pytest_item_matches_filter'
    ]
