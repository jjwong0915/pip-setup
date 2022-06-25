Pip Setup
====
Initialize a Python project with dependency management tools.

Getting Started
----
1. Create the project folder: `mkdir my-project && cd my-project`
2. Run the initialize script: `curl 'https://raw.githubusercontent.com/jjwong0915/pip-setup/main/main.py' | python3`
3. Enable the virtual environment: `source .venv/bin/activate`

Features
----
* Isolate application-specific dependencies with [venv](https://docs.python.org/3/library/venv.html)
* Generate fully-specified dependencies with [pip-tools](https://github.com/jazzband/pip-tools)

How to Add Dependencies
----
1. Add production and development dependency specifications into `requirements/base.in` and `requirements/dev.in` respectively. For example: `Django ~= 4.0`.
2. Compile the dependency specifications into requirement files: `pip-compile -o requirements/base.txt requirements/base.in && pip-compile -o requirements/dev.txt requirements/dev.in`
3. Install the compiled requirement files: `pip-sync requirements/base.txt requirements/dev.txt`
