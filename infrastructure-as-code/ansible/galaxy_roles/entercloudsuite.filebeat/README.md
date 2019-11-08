Ansible Role: filebeat 
======================================

[![Build Status](https://travis-ci.org/entercloudsuite/ansible-filebeat.svg?branch=master)](https://travis-ci.org/entercloudsuite/ansible-filebeat)
[![Galaxy](https://img.shields.io/badge/galaxy-entercloudsuite.filebeat-blue.svg?style=flat-square)](https://galaxy.ansible.com/entercloudsuite/filebeat)

# Ansible role to install & configure filebeat
Ansible role that installs filebeat on Linux using the apt package elastic provides.

Also sets up the filebeat.yml from basic vars filebeat_conf

## Requirements
Debian based Linux, tested on Ubuntu. Recent version of Ansible. Only utilized Ansible core modules.

## Role Variables

### Filebeat plain configurations
```yaml
# List of files to read logs from:
filebeat_conf:
  
  output.elasticsearch:
      hosts: ["https://localhost:9200"]
      username: "filebeat_internal"
      password: "YOUR_PASSWORD"
```

### filebeat_enable_modules
list of filebeat modules you want enable
```yaml
filebeat_enable_modules:
  - system
```

## Dependencies
This role has no dependencies to other roles.

## Example Playbook
Copy this role into the roles/mediapeers.filebeat dir in your Ansible project. Preferably add it as a submodule.
You can also install it with `ansible-galaxy install mediapeers.filebeat`.
Then use it like so:

```yaml
- name: My nice play
  hosts: servers
  roles:
  - role: ansible-filebeat
    filebeat_conf:
      output.elasticsearch:
          hosts: ["https://localhost:9200"]
          username: "filebeat_internal"
          password: "YOUR_PASSWORD"

```


## Testing

Tests are performed using [Molecule](http://molecule.readthedocs.org/en/latest/).

Install Molecule or use `docker-compose run --rm molecule` to run a local Docker container, based on the [enterclousuite/molecule](https://hub.docker.com/r/fminzoni/molecule/) project, from where you can use `molecule`.

1. Run `molecule create` to start the target Docker container on your local engine.  
2. Use `molecule login` to log in to the running container.  
3. Edit the role files.  
4. Add other required roles (external) in the molecule/default/requirements.yml file.  
5. Edit the molecule/default/playbook.yml.  
6. Define infra tests under the molecule/default/tests folder using the goos verifier.  
7. When ready, use `molecule converge` to run the Ansible Playbook and `molecule verify` to execute the test suite.  
Note that the converge process starts performing a syntax check of the role.  
Destroy the Docker container with the command `molecule destroy`.   

To run all the steps with just one command, run `molecule test`. 

In order to run the role targeting a VM, use the playbook_deploy.yml file for example with the following command: `ansible-playbook ansible-cfssl/molecule/default/playbook_deploy.yml -i VM_IP_OR_FQDN, -u ubuntu --private-key private.pem`.  

## License
BSD

