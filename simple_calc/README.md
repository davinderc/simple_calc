### CI Tools
===========
The following CI tools were found (among others) recommended by the Python Guide (https://docs.python-guide.org/scenarios/ci/):
- Jenkins
- TravisCI
- Buildbot

Buildbot seems to be an OK open-source option, but not as widely used as Jenkins and TravisCI. According to (https://www.altexsoft.com/blog/engineering/comparison-of-most-popular-continuous-integration-tools-jenkins-teamcity-bamboo-travis-ci-and-more/), Jenkins has better documentation than TravisCI and was chosen to be used first (TravisCI might be used if Jenkins presents any big obstacles). Jenkins is apparently better for big projects and TravisCI for small projects, but it seems that Jenkins is also easily run locally, while this is not clear about TravisCI in the free version.

After installing Jenkins without Docker, it seems most tutorials require one to install Docker. After installing Docker, it was clear that running Jenkins as a CI solution would take time to learn how to do and given the scope of this project, TravisCI seemed to be the better choice, since it is easy to set up and within 10 mins the repository was being tested.