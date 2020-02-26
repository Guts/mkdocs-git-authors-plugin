# Contribution Guidelines

Thanks for considering to contribute to this project!

## Testing

Make sure to install an editable version before running tests:

```python
pip install -r tests/test_requirements.txt
pip install -e .
pytest --cov=mkdocs_git_authors_plugin --cov-report term-missing test 
```

In addition, this project uses pyflakes for static code checking:

```python
pip install pyflakes
pyflakes tests/ mkdocs_git_authors_plugin/
```

## Submitting Changes

Make sure to discuss changes in an issue before putting in the work.

To get changes merged, create a pull request. 

#### Code Style

Make sure your code follows [PEP-8](https://www.python.org/dev/peps/pep-0008/) and keeps things consistent with the rest of the code. 

#### Tests

If it makes sense, writing tests for your PRs is always appreciated and will help get them merged.