[![build-test](https://github.com/darkwizard242/ansible-role-scout/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-scout/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-scout/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-scout/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/47507?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/47507?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/47507?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-scout&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-scout) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-scout&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-scout) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-scout&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-scout) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-scout&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-scout) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-scout?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-scout?color=orange&style=flat-square)

# Ansible Role: scout

Role to install (_by default_) `scout` on **Debian/Ubuntu** and **EL** systems. [Scout](https://github.com/liamg/scout) is a URL fuzzer originally developed by [Liam Galvin](https://github.com/liamg).

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
scout_app: scout
scout_version: 0.15.1
scout_os: linux
scout_arch: amd64
scout_dl_url: https://github.com/liamg/{{ scout_app }}/releases/download/v{{ scout_version }}/{{ scout_app }}-{{ scout_os }}-{{ scout_arch }}
scout_bin_path: "/usr/local/bin/{{ scout_app }}"
scout_file_owner: root
scout_file_group: root
scout_file_mode: '0755'
```

### Variables table:

Variable (default) | Description
------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------
scout_app          | Defines the app to install i.e. **scout**
scout_version      | Defined to dynamically fetch the desired version to install. Defaults to: **0.14.0**
scout_os           | Defines os type. Used for obtaining the correct type of binaries based on OS type. Defaults to: **linux**
scout_arch         | Defines os architecture. Used to set the correct type of binaries based on OS System Architecture. Defaults to: **amd64**
scout_dl_url       | Defines URL to download the scout binary from.
scout_bin_path     | Defined to dynamically set the appropriate path to store scout binary into. Defaults to (as generally available on any user's PATH): **/usr/local/bin/scout**
scout_file_owner   | Owner for the binary file of scout.
scout_file_group   | Group for the binary file of scout.
scout_file_mode    | Mode for the binary file of scout.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **scout**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.scout
```

For customizing behavior of role (i.e. specifying the desired **scout** version) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.scout
  vars:
    scout_version: 0.7.1
```

For customizing behavior of role (i.e. placing binary of **scout** package in different location) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.scout
  vars:
    scout_bin_path: /bin/
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-scout/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
