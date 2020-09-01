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

### smoothie

create:

    curl localhost:8000/smoothie/  -H "Content-Type: application/json" --data '{"name": "chilly"}'
    {"id":"c2675366-860a-40fd-9114-a6ad7bbc9d69","name":"chilly","ingredients":[]}

read:

    curl localhost:8000/smoothie/c2675366-860a-40fd-9114-a6ad7bbc9d69/  -H "Content-Type: application/json"
    {"id":"c2675366-860a-40fd-9114-a6ad7bbc9d69","name":"chilly","ingredients":[]}

update:

    curl localhost:8000/smoothie/c2675366-860a-40fd-9114-a6ad7bbc9d69/  -H "Content-Type: application/json" -X PUT --data '{"id": "c2675366-860a-40fd-9114-a6ad7bbc9d69", "name": "frigid"}'
    {"id":"c2675366-860a-40fd-9114-a6ad7bbc9d69","name":"frigid","ingredients":[]}

delete:

    curl localhost:8000/smoothie/c2675366-860a-40fd-9114-a6ad7bbc9d69/  -H "Content-Type: application/json" -X DELETE

list:

    curl localhost:8000/smoothie/ -H "Content-Type: application/json"
    [...]

### smoothie ingredient
