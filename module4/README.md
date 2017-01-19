# ia-3B5
Artificial Intelligence project

## Module 4

**Log**:
+ `Deployment.md` - document that details how deployment on AWS of the CI was made

<!-- Webpage: [2b5.github.io/ia-3B5/](https://2b5.github.io/ia-3B5/) -->

## Team members:
+ Alexandru Dan - github administration (protected master, merged branches only when integrated), AWS deployment (configured AWS EC2 instance and Jenkins CI tasks and security for multiple users), initial code/tests for teams (`../demos`), manual testing and report (started automatic testing with Protractor)
+ Alexii Georgiana - manual testing
+ Luca Iulian - manual testing and report
+ Sandu Daniel - manual testing

#### Folder structure (example):
+ `nltk/` and `pycore/` - implementations - tokenize and lemmatize
  + both have tests, which you can run by: `py -2.7 test_sample.py [-v]` (verbose argument optional)

## Resources and tehnologies


## Useful Links
+ folder structure and other tips & tricks: http://docs.python-guide.org/en/latest/writing/structure/
+ logging - https://docs.python.org/2/howto/logging.html
+ unit testing in python:
  + https://docs.python.org/2/library/unittest.html
  + http://pythontesting.net/framework/unittest/unittest-introduction/
  + http://www.onlamp.com/pub/a/python/2004/12/02/tdd_pyunit.html
  + http://www.diveintopython.net/unit_testing/index.html#roman.intro
  + http://docs.python-guide.org/en/latest/writing/tests/
  + http://www.drdobbs.com/testing/unit-testing-with-python/240165163
  + https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/
  + https://stackoverflow.com/questions/1732438/how-to-run-all-python-unit-tests-in-a-directory
+ code coverage module: https://coverage.readthedocs.io/en/latest/
