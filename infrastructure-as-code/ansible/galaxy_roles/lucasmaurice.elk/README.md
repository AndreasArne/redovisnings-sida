# Ansible Role: Elastic Stack [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Build Status](https://travis-ci.org/lucasmaurice/ansible-role-elk.svg?branch=master)](https://travis-ci.org/lucasmaurice/ansible-role-elk)

Install a dockerized version of the [Elastic Stack](https://www.elastic.co/products/). Role based on the *Docker Compose* presented by [Anthony Lapenna](https://github.com/deviantony) [here](https://github.com/deviantony/docker-elk).

## Role Dependancies

- **Docker** deployed on the host (Tested with [lucasmaurice.ansible_role_docker](https://galaxy.ansible.com/lucasmaurice/ansible-role-docker/))

## Role Variables

Available variables are listed below, along with default values (see defaults/main.yml):

```yaml
---

```

## Example Playbook

This is an example of how to use this role:

```yaml
    - hosts: monitoring
        roles:
            - docker
            - { role: elk }
```

## License

MIT
