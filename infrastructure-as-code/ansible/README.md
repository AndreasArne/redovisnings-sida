## Ansible vault

Add Ansible vault password as ENV variable, `ANSIBLE_VAULT_PASSWORD_FILE=<path-to-file>`. 
I had to run file as bash script for it to work.
```
#!/bin/bash
cat <<EOF
<password>
EOF
```



## AWS credentials

Use `insert_aws_keys_in_config.sh` to paste AWS credentials from clipboard into `aws_keys.yml`.



## ansible.cfg

Config for ansible.
Needed the following for Ansible to read the `hosts` file (which parser it should use to read the file).
```
[inventory]
enable_plugins = ini
```

To be able to run Ansible from a venv, the following is needed.
```
ansible_python_interpreter = ../../.venv/bin/python
```



## Run locally

When we want to work against an API, as the AWS modules do, we don't want Ansible to SSH to any server. So we connect to localhost without an ssh connection.
In `hosts` we need:
```
[local]
localhost ansible_connection=local
```
In the playbook:
```
-   hosts: local
    connection: local # Keep ansible from open ssh connection
    gather_facts: False
```