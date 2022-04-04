import os.path

__all__ = [
    "__title__",
    "__summary__",
    "__uri__",
    "__version__",
    "__commit__",
    "__author__",
    "__email__",
    "__license__",
    "__copyright__",
]


try:
    base_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    base_dir = None


__title__ = "dev_review"
__summary__ = "guide to code review during research"
__uri__ = "https://github.com/ResearchCodeReviewCommunity/dev-review"

__version__ = "0.1.0"

if base_dir is not None and os.path.exists(os.path.join(base_dir, ".commit")):
    with open(os.path.join(base_dir, ".commit")) as fp:
        __commit__ = fp.read().strip()
else:
    __commit__ = None

__author__ = "Research Code Review Community"
__email__ = "fergus.cooper@cs.ox.ac.uk"

__license__ = "MIT"
__copyright__ = "2020-present %s" % __author__
