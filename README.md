# ansible-role-airflow

This is an Ansible role for the [Apache Airflow][airflow] platform.

## Development Environment

One can use [Vagrant][vagrant] to create virtual machines for development and
test. More information on this topic can be found in the official [Vagrant
Documentation][vagrant-documentation], the [Cheat Sheet][vagrant-cheat-sheet]
and the `Vagrantfile` in this project.

## Role Parameters

Available role customization parameters, together with default values, can be
found in the accompanying `defaults/main.yml` file.

## Securing Connections Passwords

Airflow can encrypt passwords of the connections within the metadata database.
To enable this feature the `apache-airflow[crypto]` package needs to be
installed and the `fernet_key` (`airflow_configuration` dictionary in
`defaults/main.yml`) configuration option has to be provided.

See [Securing Connections section][airflow-securing] of the official Apache
Airflow documentation for instructions how to generate the `fernet_key`.

[airflow]: https://airflow.apache.org/
[airflow-securing]: https://airflow.apache.org/howto/secure-connections.html
[vagrant]: https://vagrantup.com/
[vagrant-documentation]: https://vagrantup.com/docs/
[vagrant-cheat-sheet]: https://gitlab.com/eyeo/devops/ansible-role-example/wikis/vagrant
