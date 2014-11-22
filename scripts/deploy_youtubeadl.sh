#!/bin/bash

cd ../ansible

ansible-playbook -i www.youtubeadl.com, ../ansible/production.yml --tags="deploy" --ask-vault-pass

