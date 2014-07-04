#!/bin/bash

cd ../ansible

ansible-playbook -i www.youtubeadl.com, production.yml --tags="deploy" --ask-vault-pass

