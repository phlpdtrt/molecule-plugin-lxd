[![tox](https://github.com/phlpdtrt/molecule-plugin-lxd/actions/workflows/tox.yml/badge.svg)](https://github.com/phlpdtrt/molecule-plugin-lxd/actions/workflows/tox.yml)

# molecule-plugin-lxd

This repository contains the lxd molecule plugin


## Installation

```bash
pip3 install molecule-plugin-lxd
```


## Usage

example molecule configuration

```bash
---
dependency:
  name: galaxy
driver:
  name: lxd
lint: |
  set -e
  yamllint .
  ansible-lint
platforms:
  - name: instance
    source:
      alias: ubuntu/jammy/amd64
provisioner:
  name: ansible
verifier:
  name: ansible
```
