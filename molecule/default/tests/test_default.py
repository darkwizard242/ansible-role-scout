import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_scout_binary_exists(host):
    assert host.file('/usr/local/bin/scout').exists


def test_scout_binary_file(host):
    assert host.file('/usr/local/bin/scout').is_file


def test_scout_binary_which(host):
    assert host.check_output('which scout') == '/usr/local/bin/scout'
