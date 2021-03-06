from urllib.parse import urljoin

from pulp_smash.constants import PULP_FIXTURES_BASE_URL  # noqa:F401
from pulp_smash.pulp3.constants import (  # noqa:F401
    BASE_PUBLISHER_PATH,
    BASE_REMOTE_PATH,
    CONTENT_PATH
)

ANSIBLE_ROLE_CONTENT_PATH = urljoin(CONTENT_PATH, 'ansible/roles/')
ANSIBLE_ROLE_VERSION_CONTENT_PATH = urljoin(CONTENT_PATH, 'ansible/roles/versions/')

ANSIBLE_REMOTE_PATH = urljoin(BASE_REMOTE_PATH, 'ansible/')

ANSIBLE_PUBLISHER_PATH = urljoin(BASE_PUBLISHER_PATH, 'ansible/')


ANSIBLE_GALAXY_URL = 'https://galaxy.ansible.com/api/v1/roles/'

NAMESPACE_ANSIBLE = '?namespace__name=ansible'
NAMESPACE_PULP = '?namespace__name=pulp'

ANSIBLE_FIXTURE_URL = urljoin(ANSIBLE_GALAXY_URL, NAMESPACE_ANSIBLE)
ANSIBLE_PULP_FIXTURE_URL = urljoin(ANSIBLE_GALAXY_URL, NAMESPACE_PULP)

ANSIBLE_FIXTURE_CONTENT_SUMMARY = {
    "ansible-role-version": 5,
}
ANSIBLE_FIXTURE_COUNT = 5

ANSIBLE_PULP_FIXTURE_CONTENT_SUMMARY = {
    "ansible-role-version": 3,
}
ANSIBLE_PULP_FIXTURE_COUNT = 3


# FIXME: replace this with the location of one specific content unit of your choosing
ANSIBLE_URL = urljoin(ANSIBLE_FIXTURE_URL, '')
