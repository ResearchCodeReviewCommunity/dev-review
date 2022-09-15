import os
import pathlib

import nox

VENV_DIR = pathlib.Path('./.venv').resolve()


@nox.session
def dev(session: nox.Session) -> None:
    """
    Sets up a python development environment for the project.
    This session will:
    - Create a python virtualenv for the session
    - Install the `virtualenv` cli tool into this environment
    - Use `virtualenv` to create a global project virtual environment
    - Invoke the python interpreter from the global project environment to install
      the project and all it's development dependencies.
    """

    session.install("virtualenv")
    # VENV_DIR here is a pathlib.Path location of the project virtualenv
    # e.g. .venv
    session.run("virtualenv", os.fsdecode(VENV_DIR), silent=True)

    python = os.fsdecode(VENV_DIR.joinpath("bin/python"))

    # Use the venv's interpreter to install the project along with
    # all it's dev dependencies, this ensures it's installed in the right way
    session.run(python, "-m", "pip", "install", "-e", ".[docs]", external=True)


@nox.session
def docs(session: nox.Session) -> None:
    """
    Build the docs. Pass "serve" to serve. Pass "autobuild" to run ``sphinx-autobuild``.
    """
    if session.posargs:
        if "autobuild" in session.posargs:
            # autobuild does the build bit, too
            session.install(".[docs]")
            session.run("sphinx-autobuild", "docs", "docs/_build/html")
        elif "serve" in session.posargs:
            session.install(".[docs]")
            session.chdir("docs")
            session.run("sphinx-build", "-M", "html", ".", "_build")

            print("Launching docs at http://localhost:8000/ - use Ctrl-C to quit")
            session.run("python", "-m", "http.server", "8000", "-d", "_build/html")
        else:
            print("Unsupported argument to docs")
    else:
        session.install(".[docs]")
        session.chdir("docs")
        session.run("sphinx-build", "-M", "html", ".", "_build")
