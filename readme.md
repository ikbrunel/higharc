# Higharc Full Stack Engineer Challenge

Brought to you by Benjamin Vulpes

## 🚂🚂🚂

This is a python 3 project.

Something along the lines of the following should get you rolling:

    brew install python3
    pip3 install virtualenvwrapper  # hopefully your distro or homebrew brings pip3 along with py3
    mkvirtualenv higharc_bv  # install packages locally; for subsequent runs use `workon higharc_bv`
    cd $WHEREVER_THIS_REPO_IS_ON_DISC
    pip install -r requirements.txt  # install deps
    ./manage.py runserver

## examples:

create:

    curl localhost:8000/smoothie/ --data '{"name": "dank", "ingredients": [{"name": "foo", "quantity": 1}]}' -H "Content-Type: application/json"

    -> {"id":"219b2799-aef9-42fd-8bc7-2d95f73c3dc4","name":"dank","ingredients":[{"id":"e6c7bb62-3037-4a28-828a-b24687770f18","name":"foo","quantity":1}]}

read:

    curl -H "Content-Type: application/json" localhost:8000/smoothie/219b2799-aef9-42fd-8bc7-2d95f73c3dc4/

    -> {"id":"219b2799-aef9-42fd-8bc7-2d95f73c3dc4","name":"dank","ingredients":[{"id":"e6c7bb62-3037-4a28-828a-b24687770f18","name":"foo","quantity":1}]}

update:



delete:

    curl -X DELETE localhost:8000/smoothie/$SMOOTHIE_ID
