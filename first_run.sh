#!/usr/bin/env bash -xeu

workon higharc_bv  # please work through the readme.md; provisioning a dev env is out of scope for this engineering challenge
psql -c 'create database higharc_bv'
./manage.py migrate
