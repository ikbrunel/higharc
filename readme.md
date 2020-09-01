# Higharc Full Stack Engineer Challenge

Brought to you by Benjamin Vulpes

## 🚂🚂🚂

This is a python 3 project.

Something along the lines of the following should get you rolling:

    brew install python3
    pip3 install virtualenvwrapper  # hopefully your distro or homebrew brings pip3 along with py3
    mkvirtualenv higharc_bv  # install packages locally; for subsequent runs use `workon higharc_bv`
    cd $WHEREVER_THIS_REPO_IS_ON_DISC
    pip3 install -r requirements.txt  # install deps
    ./manage.py runserver

## TODO

1. Implement users.
1. Implement partial updates.
1. Refactor `url` on test classes onto the class instance and out of test bodies.

## examples:

May be somewhat out of date, but should serve as an adequate map, if not "build-ready" plans.

### smoothie

create:

    curl localhost:8000/smoothie/  -H "Content-Type: application/json" --data '{"name": "chilly"}'
    {"id":"c2675366-860a-40fd-9114-a6ad7bbc9d69","name":"chilly","ingredients":[]}

read:

    curl -H "Content-Type: application/json" localhost:8000/smoothie/caf50cb1-d0de-49d1-97dc-f18caa483b41/
    {"id":"caf50cb1-d0de-49d1-97dc-f18caa483b41","name":"chilly","ingredients":["d73b1bf4-760d-45f7-961f-e4c18b9f8090"]}

update:

    curl localhost:8000/smoothie/c2675366-860a-40fd-9114-a6ad7bbc9d69/  -H "Content-Type: application/json" -X PUT --data '{"id": "c2675366-860a-40fd-9114-a6ad7bbc9d69", "name": "frigid"}'
    {"id":"c2675366-860a-40fd-9114-a6ad7bbc9d69","name":"frigid","ingredients":[]}

delete:

    curl localhost:8000/smoothie/c2675366-860a-40fd-9114-a6ad7bbc9d69/  -H "Content-Type: application/json" -X DELETE

list:

    curl localhost:8000/smoothie/ -H "Content-Type: application/json"
    [...]

### smoothie ingredient

create:

    curl localhost:8000/ingredient/ -H "Content-Type: application/json" --data '{"name": "ice cubes", "quantity": 4, "smoothie": "caf50cb1-d0de-49d1-97dc-f18caa483b41"}'
    {"id":"5dd8d999-d944-4042-9e9d-acf4d2f5ebc1","name":"ice cubes","quantity":4,"smoothie":"caf50cb1-d0de-49d1-97dc-f18caa483b41"}


read:

    curl localhost:8000/ingredient/5dd8d999-d944-4042-9e9d-acf4d2f5ebc1/ -H "Content-Type: application/json"
    {"id":"5dd8d999-d944-4042-9e9d-acf4d2f5ebc1","name":"ice cubes","quantity":4,"smoothie":"caf50cb1-d0de-49d1-97dc-f18caa483b41"}

update:

    curl localhost:8000/ingredient/5dd8d999-d944-4042-9e9d-acf4d2f5ebc1/ -H "Content-Type: application/json" -X PUT --data '{"id": "5dd8d999-d944-4042-9e9d-acf4d2f5ebc1", "name": "tiny cubes", "quantity": 4, "smoothie": "caf50cb1-d0de-49d1-97dc-f18caa483b41"}'
    {"id":"5dd8d999-d944-4042-9e9d-acf4d2f5ebc1","name":"tiny cubes","quantity":4,"smoothie":"caf50cb1-d0de-49d1-97dc-f18caa483b41"}

delete:

    curl localhost:8000/ingredient/5dd8d999-d944-4042-9e9d-acf4d2f5ebc1/ -H "Content-Type: application/json" -X DELETE

list:

    curl localhost:8000/ingredient/ -H "Content-Type: application/json"
    [...]
