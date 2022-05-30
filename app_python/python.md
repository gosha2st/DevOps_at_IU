# Best practices for a Python web application

## General code writing and styling
1. Follow guidelines from *PEP 8 - The Official Style Guide for Python Code*:  
http://python.org/dev/peps/pep-0008/
2. Follow other popular and commonly-accepted **guidelines** on code writing in Python, such as:
    * *PEP 20 - The Zen of Python*:  
http://python.org/dev/peps/pep-0020/
    * *BOBP Guide for Python*:  
http://gist.github.com/sloria/7001839
    * *Google Python Style Guide*:  
http://google.github.io/styleguide/pyguide.html
    * *The Hitchhiker’s Guide to Python*:  
http://docs.python-guide.org/
    * *PEP 257 - Docstring Conventions* (for proper Documentation):  
http://python.org/dev/peps/pep-0257/
    * *Sphinx Style Guide*:  
http://pythonhosted.org/an_example_pypi_project/sphinx.html
    * *Numpy Style Guide*:  
http://numpydoc.readthedocs.io/en/latest/format.html
    * Aggregated advises and tips, such as:
        * http://berknology.medium.com/python-coding-best-practices-f3e24a958ad4
        * http://data-flair.training/blogs/python-best-practices/
        * http://realpython.com/python-code-quality/
        * http://dzone.com/articles/7-best-python-code-review-tools-recommended-by-dev
        * http://luminousmen.com/post/python-static-analysis-tools
        * http://nerdwallet.com/blog/engineering/5-pytest-best-practices/
        * http://medium.com/worldsensing-techblog/tips-and-tricks-for-unit-tests-b35af5ba79b1
        * and others.
3. Always **refer to common sense** and apply all previously and subsequently listed guidelines only as long as sensible.
4. Maintain proper, clear, and yet simple **documentation**.
5. Make use of *linters* and other **static analysis tools** wherever possible, such as:
    * *PyLint*: http://pylint.org/
    * *Darglint*: http://github.com/terrencepreilly/darglint
    * *Pyflakes*: http://github.com/PyCQA/pyflakes
    * *pycodestyle (pep8)*: http://github.com/PyCQA/pycodestyle
    * *Prospector*: http://prospector.landscape.io/en/master/
    * *bandit*: http://github.com/PyCQA/bandit
    * *mypy*: http://mypy.readthedocs.io/en/
    * *safety*: http://github.com/pyupio/safety
    * *SonarQube*: http://sonarqube.org/
    * and others.
6. Use well-tested and production ready **frameworks**, such as:
    * *Django*: http://djangoproject.com/
    * *Flask*: http://flask.palletsprojects.com/
    * *FastAPI*: http://fastapi.tiangolo.com/
    * *Sanic*: http://sanicframework.org/en/
    * etc.
7. Apply **formatting tools**, such as:
    * *black*: http://github.com/psf/black
    * *isort*: http://github.com/PyCQA/isort
    * *pyupgrade*: http://github.com/asottile/pyupgrade
    * *editorconfig*: http://editorconfig.org/
    * etc.
8. Consider ready-to-use *pre-commit* **hooks** with code-formatting -- a framework for managing and maintaining multi-language pre-commit hooks: http://pre-commit.com/
9. Introduce two running scripts -- for development and production modes.
10. Use production-ready WSGI server (*Gunicorm*) instead of Flask development server in production.

## Project management
1. Create and maintain the `README` file.
2. Create and maintain the `requirements.txt` file for Python packages.
3. Utilize *git* for better version control.
4. Add `.gitignore` to exclude irrelevant files from the Git VCS.  
gitignore.io can be used to generate *gitignore* files for popular tools.
5. Include `.dockerignore` to reduce docker context size.
6. Same for `.editorconfig`.
7. Check `lockfile` into version control to ensure reproducible builds locally and in CI.
8. Introduce dependency management utility, such as:
    * *Pipenv*: http://docs.pipenv.org/
    * *Poetry*: http://python-poetry.org/
    * etc.
9. Place files into appropriate folders and functions into appropriate modules.
10. Partition distinct projects into separate virtual environments to prevent version conflicts.

## Tests and unit testing
1. Strive for 100% code coverage, but don't get obsess over the coverage score.
2. Test each little piece of software independently.
3. Tests should be isolated and fully independent:
    * They should pass regardless the order of execution.
    * They should run on a fresh dataset every time.
    * Do not interact with a real database or network.
    * Use a separate test database that gets torn down or use mock objects.
4. Do not modify the application code in tests.
5. Use one testcase class for a single class or model.
6. Never manually create `Response` objects for tests.
7. Parametrize your tests.  
Do not use the same test copy-pasted many times with different inputs.
8. Follow the *Given-When-Then* style of writing tests: http://martinfowler.com/bliki/GivenWhenThen.html
9. Use ready-made testing frameworks, for example *PyTest*: http://docs.pytest.org/en/
10. Consider using *Test Driven Development (TDD)*.
11. Introduce *Functional Tests* for web and GUI applications to simulate end-user behaviour.
12. Separate between *Unit* and *Functional Tests*.
13. Use *fixtures* to provide common setup and teardown code.
14. Use *yield fixtures*.
15. Do not modify fixtures in other fixtures.
16. But better prefer *factories* over *fixtures*:
http://github.com/FactoryBoy/factory_boy
17. Prefer `tmpdir` over global test artifacts.
18. Add running tests into *pre-commit* hooks, so that developers do not push broken code.  
(Only in case the number of test is not huge!)
19. Write tests as scenarios. Testcase and test method names should read like a scenario description.
20. Treat test code as core code. Make your test code readable, use docstrings and comments and respect style, almost as if it was a part of the functional code base.
21. Refer to online guidelines, such as:
    * General:
        * *Python Code Quality: Tools & Best Practices*:  
http://realpython.com/python-code-quality/
    * PyTest:
        * *Effective Python Testing With Pytest*:  
http://realpython.com/pytest-python-testing/
        * *Tips and tricks for unit tests (with Python & Pytest)*:  
http://medium.com/worldsensing-techblog/tips-and-tricks-for-unit-tests-b35af5ba79b1
        * *5 Pytest Best Practices for Writing Great Python Tests*:  
http://nerdwallet.com/blog/engineering/5-pytest-best-practices/
    * Flask:
        * *Testing Flask Applications* official guideline:  
http://flask.palletsprojects.com/en/2.0.x/testing/
        * *Guide to Python Flask Unit Testing*:  
http://codethechange.stanford.edu/guides/guide_flask_unit_testing.
        * *Testing Flask Applications with Pytest*:  
http://testdriven.io/blog/flask-pytest/
        * *Unit Testing a Flask Application*:  
http://patricksoftwareblog.com/unit-testing-a-flask-application/
        * *The Flask Mega-Tutorial, Part VII: Unit Testing*:  
http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-unit-testing-legacy
    * and others:
        * *Testing Best Practices for Machine Learning Libraries*:  
http://towardsdatascience.com/testing-best-practices-for-machine-learning-libraries-41b7d0362c95
        * etc.
