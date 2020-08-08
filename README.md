[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-scout.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-scout) ![Ansible Role](https://img.shields.io/ansible/role/47507?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/47507?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/47507?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-scout&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-scout) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-scout?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-scout?color=orange&style=flat-square)

# Ansible Role: scout

Role to install (_by default_) `scout` on **Debian/Ubuntu** and **EL** systems. [Scout](https://github.com/liamg/scout) is a URL fuzzer originally developed by [Liam Galvin](https://github.com/liamg).

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
scout_app: scout
scout_version: 0.10.0
scout_osarch: linux-amd64
scout_dl_url: https://github.com/liamg/{{ scout_app }}/releases/download/v{{ scout_version }}/{{ scout_app }}-{{ scout_osarch }}
scout_bin_path: "/usr/local/bin/{{ scout_app }}"
scout_bin_permission_mode: '0755'
```

### Variables table:

Variable                  | Value (default)                                                                                                      | Description
------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------
scout_app                 | scout                                                                                                                | Defines the app to install i.e. **scout**
scout_version             | 0.10.0                                                                                                               | Defined to dynamically fetch the desired version to install. Defaults to: **0.10.0**
scout_osarch              | linux-amd64                                                                                                          | Defines os architecture. Used for obtaining the correct type of binaries based on OS System Architecture. Defaults to: **linux-amd64**
scout_dl_url              | <https://github.com/liamg/{{> scout_app }}/releases/download/v{{ scout_version }}/{{ scout_app }}-{{ scout_osarch }} | Defines URL to download the scout binary from.
scout_bin_path            | "/usr/local/bin/{{ scout_app }}"                                                                                     | Defined to dynamically set the appropriate path to store scout binary into. Defaults to (as generally available on any user's PATH): **/usr/local/bin/scout**
scout_bin_permission_mode | '0755'                                                                                                               | Defines the permission mode level for the file.

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

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
