# Higharc Full Stack Engineer Challenge

Brought to you by Benjamin Vulpes

# Intro

Good day, friends at Higharc! I present to you my crack at your Full Stack Engineer Challenge.

## Dependencies

I elected to take 3 dependencies:
- Django
- Django REST Framework
- psycopg2

Django is the heavy hitter of Python web frameworks. It can be set up to do form-heavy postback CRUD apps, websocketry, and (with the Django REST Framework package), speedy and concise API development. At a high level, I took a dependency on it because I know it quite well, and I wanted to take the opportunity to show you a well-structured and easily understood project rather than spend a bunch of time reimplementing low-level concerns. Concretely, I wanted to take advantage of Django's Object/Relational Model to abstract over the database, and make quick progress on building out the API functionality for your challenge.

Django REST Framework leverages the Django ORM for API validation, error messages, and object relationships. It's tightly coupled to REST semantics and implements a great deal of the important machinery one wants in production (JWT, session-based authentication, versioning, throttling, and so on), and I took a dependency on it so that I could focus on making headway against the design requirements instead of miring myself down in marshalling dictionaries into and out of JSON.

psycopg2 is the database library for Postgres, not much interesting there.

## Features/Implementations

I sought with this project to deliver a hardened REST API that covers a Smoothie resource and a SmoothieIngredient resource. Both resources implement the full CRUDL interface, and both resources share some lightweight authentication logic to ensure that clients can only see their own smoothies and smoothie ingredients, and can't mess with anyone else's smoothies. In detail:

- Users can create, read, update, delete, and list their smoothies.
- Smoothie names are unique.
- Users can create, read, update, delete, and list their smoothie ingredients (including associating their smoothie ingredients with a smoothie).
- Users can only see and mutate *their* smoothies.
- The API is deployed to EC2 with Elastic Beanstalk, and uses RDS for the data store.
- The API has pretty good test coverage for the time allocated to the project.
- The data model uses UUIDs for primary keys to forestall enumerability.

## Design Refinements

It's fun to think about how requirements might change for a service like this in the wild. Here are a few notions!

- It might be useful to move from FKs from ingredients to smoothies, to a M2M model, where ingredients can show up on multiple smoothies.
- It would be cool for people to share their smoothies around; we can model this with a join table defining which users can perform which actions on which smoothies. We'd want to be careful in the UI design about giving users the ability to mark their smoothies as further shareable, though!

## Production Hardening

The deployment story for this app is pretty good out of the box (thanks, Elastic Beanstalk!): DB connection secrets are emplaced in the AWS console and available to the containers at runtime. The development workflow is pretty good, with a solid set of tests and a red/green/refactor loop that worked quite well for me while I was working on it (I've grown spoiled by the corporate Intellij UE license, and having to boot my Emacs Python stack back up for this challenge was fun. Good thing all of my config files are versioned!). There are a few things we'd want to take care of before exposing this service to the world:

- implement CI/CD

    Peter mentioned that y'all have your delivery story totally sorted out, and frankly I'd rather do less dev/ops and more software engineering, so I focused on a tightly-factored final product demonstrating abstract software engineering competence instead of building out CI/CD pipelines.

- fix static assets

    Not a big deal at all, since this is ultimately an API. However, DRF has a charming web UI to the REST endpoints that it exposes, and I would have been very pleased to have gotten those working as well.

- stand up our own PyPI

    One should have ones own package index. PyPI doesn't go down nearly as much as some other package repositories that are out there, but it happens. Moreover, one wants strict control over packages released to prod.

- stand up a staging environment

    I always end up wanting one :D

- TLS

    Table stakes in 2020!

## What went well

- Data model design and implementation

    Two tables, came together pretty quickly.

- REST endpoints

    DRF is pretty great for knocking out CRUD endpoints based on Django models. Frankly, though, I'm looking forward to getting spun up on a new programming ecosystem. Validation logic to differentiate between users was easy to implent with the Django ORM.

- "Authentication" implementation.

    Authentication came together reasonably quickly as well; aided hugely by the fact that I'd already codified the API's behavior in a small test suite, and so could go audit each subset of behaviors and get high confidence that my implementation was correct, and quick feedback when it wasn't.

- Tests

    I love tests. It's possibly Stockholm syndrome from working in untyped environments for so long. If we work together, I will be *thrilled* to jump into the world of Typescript.

## What went poorly

It would be disingenous to imply that this project came together with no tears. While the core of this project is entirely within my wheelhouse, I did got a bit too bold for the timeline in 2 cases, and had to back out of both.

- ECS pipeline

    I burned a horrendous amount of time setting up an ECS pipeline, and nearly threw my laptop out a window getting CodeDeploy to run the containers I'd already set up the builds for in CodeBuild. Elastic Beanstalk took maybe twenty minutes to serve HTML. That HTML was an error page, but that was still miles ahead of where I'd landed with CodePipeline.

- Nested resources

    I also lost a fair amount of time trying to pull off something clever, and get the API to support nested CRUD. I was shooting for a single interface to the data model where one could update ingredients and smoothie data all in one shot. I got bogged down in incidential complexities, backed out, and in short order had functional separate endpoints for each resource.

## Summa

Thank you for taking the time to read this wall of text, and to consider me for a position at Higharc! I hope that this repo and the discussion above convinces you that I am a pragmatic and focused engineer, with demonstrable design and implementation chops. This project is all in Python, but I look forward to booting up on a Typescript project soon :)

Yours,
Benjamin

# Technicalia

## 🚂🚂🚂

This is a python 3 project.

Something along the lines of the following should get you rolling:

    brew install python3
    pip3 install virtualenvwrapper  # hopefully your distro or homebrew brings pip3 along with py3
    mkvirtualenv higharc_bv  # install packages locally; for subsequent runs use `workon higharc_bv`
    cd $WHEREVER_THIS_REPO_IS_ON_DISC
    pip3 install -r requirements.txt  # install deps
    psql -c 'create database higharc_bv'  # you will want a postgres
    ./manage.py migrate
    ./manage.py runserver

## TODO

1. Update documentation to show user_id usage.
1. Implement partial updates.
   It would be very convenient for users to supply only the data that they want to change, instead of the whole object.
1. Fix staticfiles.
   Also an aesthetic concern, but since people look at the various frontend pages, would be nice.
1. Refactor `url` on test classes onto the class instance and out of test bodies.
   Entirely an aesthetic concern.
1. Refactor the UUID PK field into a reusable field.
   If this API were to continue growing, we'd want to factor the UUID PK fields out and have one definition used across the whole codebase.
1. Add database constraints to ensure that user_ids match on associated smoothies and items (this currently is only enforced in application code).
1. Add test-running to Elastic Beanstalk deploy

## examples:

### smoothie

create:

    curl -H "Content-Type: application/json" \
    http://higharc-env.eba-ry2sev3p.us-east-1.elasticbeanstalk.com/smoothie/ \
    --data '{"name": "chilly smoothie", \
             "user_id": "0a819266-420a-43b6-b677-aac44a8bb0e1"}'

    {"id":"28808d54-9a46-44d7-9c90-632e2c144584", \
     "name":"chilly smoothie", \
     "ingredients":[], \
     "user_id":"0a819266-420a-43b6-b677-aac44a8bb0e1"}

read:

    curl -H "Content-Type: application/json" \
    http://higharc-env.eba-ry2sev3p.us-east-1.elasticbeanstalk.com/smoothie/28808d54-9a46-44d7-9c90-632e2c144584/?user_id=0a819266-420a-43b6-b677-aac44a8bb0e1

    {"id":"28808d54-9a46-44d7-9c90-632e2c144584", \
     "name":"chilly smoothie", \
     "ingredients":[], \
     "user_id":"0a819266-420a-43b6-b677-aac44a8bb0e1"}

update:

    curl -H "Content-Type: application/json" -X PUT \
    http://higharc-env.eba-ry2sev3p.us-east-1.elasticbeanstalk.com/smoothie/28808d54-9a46-44d7-9c90-632e2c144584/ \
    --data '{"name": "frigid smoothie", \
             "user_id": "0a819266-420a-43b6-b677-aac44a8bb0e1"}'

    {"id":"28808d54-9a46-44d7-9c90-632e2c144584", \
     "name":"frigid smoothie", \
     "ingredients":[], \
     "user_id":"0a819266-420a-43b6-b677-aac44a8bb0e1"}

delete:

    curl -H "Content-Type: application/json" -X DELETE \
    http://higharc-env.eba-ry2sev3p.us-east-1.elasticbeanstalk.com/smoothie/28808d54-9a46-44d7-9c90-632e2c144584/

list:

    curl -H "Content-Type: application/json" \
    http://higharc-env.eba-ry2sev3p.us-east-1.elasticbeanstalk.com/smoothie/?user_id=0a819266-420a-43b6-b677-aac44a8bb0e1

    [{"id":"28808d54-9a46-44d7-9c90-632e2c144584", \
      "name":"frigid smoothie", \
      "ingredients":[], \
      "user_id":"0a819266-420a-43b6-b677-aac44a8bb0e1"}]

### smoothie ingredient

create:

    curl -H "Content-Type: application/json" \
    http://higharc-env.eba-ry2sev3p.us-east-1.elasticbeanstalk.com/ingredient/ \
    --data '{"name": "ice cubes", "quantity": 4, \
             "smoothie": "28808d54-9a46-44d7-9c90-632e2c144584", \
             "user_id": "0a819266-420a-43b6-b677-aac44a8bb0e1"}'

    {"id":"0b285a1f-1615-420e-98aa-a478260c6aa6", \
     "name":"ice cubes", \
     "quantity":4, \
     "smoothie":"28808d54-9a46-44d7-9c90-632e2c144584", \
     "user_id":"0a819266-420a-43b6-b677-aac44a8bb0e1"}

read:

    curl -H "Content-Type: application/json" \
    http://higharc-env.eba-ry2sev3p.us-east-1.elasticbeanstalk.com/ingredient/0b285a1f-1615-420e-98aa-a478260c6aa6/?user_id=0a819266-420a-43b6-b677-aac44a8bb0e1

    {"id":"0b285a1f-1615-420e-98aa-a478260c6aa6", \
     "name":"ice cubes", \
     "quantity":4, \
     "smoothie":"28808d54-9a46-44d7-9c90-632e2c144584", \
     "user_id":"0a819266-420a-43b6-b677-aac44a8bb0e1"}

update:

    curl -H "Content-Type: application/json" -X PUT \
    http://higharc-env.eba-ry2sev3p.us-east-1.elasticbeanstalk.com/ingredient/0b285a1f-1615-420e-98aa-a478260c6aa6/ \
    --data '{"name": "sonic ice", \
             "quantity": 5, \
             "smoothie":"28808d54-9a46-44d7-9c90-632e2c144584", \
             "user_id": "0a819266-420a-43b6-b677-aac44a8bb0e1"}'

    {"id":"0b285a1f-1615-420e-98aa-a478260c6aa6", \
     "name":"sonic ice", \
     "quantity":5, \
     "smoothie":"28808d54-9a46-44d7-9c90-632e2c144584", \
     "user_id":"0a819266-420a-43b6-b677-aac44a8bb0e1"}

delete:

    curl -X DELETE -H "Content-Type: application/json" -X PUT \
    http://higharc-env.eba-ry2sev3p.us-east-1.elasticbeanstalk.com/ingredient/0b285a1f-1615-420e-98aa-a478260c6aa6/?user_id=0a819266-420a-43b6-b677-aac44a8bb0e1

list:

    curl -H "Content-Type: application/json" \
    http://higharc-env.eba-ry2sev3p.us-east-1.elasticbeanstalk.com/ingredient/?user_id=0a819266-420a-43b6-b677-aac44a8bb0e1

    [{"id":"0b285a1f-1615-420e-98aa-a478260c6aa6", \
      "name":"sonic ice", \
      "quantity":5, \
      "smoothie":"28808d54-9a46-44d7-9c90-632e2c144584", \
      "user_id":"0a819266-420a-43b6-b677-aac44a8bb0e1"}]
