<div align="center">
  <h1>Django docmanager</h1>

  <p>
    <strong>A django learning exercise</strong>
  </p>

  <a href="https://django-docmanager.herokuapp.com">django-docmanager.herokuapp.com</a>
</div>

A restful api for managing documents with django rest framework. No auth/permissions are implemented.

## Endpoints
  - [/docs](https://django-docmanager.herokuapp.com/docs)
    > GET / POST documents
  - [/docs/:uuid4](https://django-docmanager.herokuapp.com/docs/bce30b6a-17b5-4803-87e5-2edb53ab5515/)
    > GET / PUT / DELETE a document
  - [/companies](https://django-docmanager.herokuapp.com/companies/)
    > GET / POST companies
  - [/companies/:name](https://django-docmanager.herokuapp.com/companies/ZapSign/)
    > GET / PUT / DELETE a company
  - [/companies/:name/docs](https://django-docmanager.herokuapp.com/companies/ZapSign/docs/)
    > GET documents from a company
  - [/users](https://django-docmanager.herokuapp.com/users/)
    > GET / POST users
  - [/users/:email](https://django-docmanager.herokuapp.com/users/admin@zapsign.com.br/)
    > GET / PUT / DELETE a user
  - [/users/id/:id](https://django-docmanager.herokuapp.com/users/id/1/)
    > GET / PUT / DELETE a user
  - [/users/:email/docs](https://django-docmanager.herokuapp.com/users/admin@zapsign.com.br/docs/)
    > GET documents from a user
  - [/users/id/:id/docs](https://django-docmanager.herokuapp.com/users/id/1/docs/)
    > GET documents from a user

## Setup

1. Clone the repository
  
  ```zsh
  git clone git@github.com:pedrossdemelo/django-docmanager.git
  ```

2. Setup the virtual environment
  
  ```zsh
  python -m venv .venv && source .venv/bin/activate
  ```

3. Install dependencies
  
  ```zsh
  pip install -r requirements.txt
  ```

4. [Install postgresql on your machine](https://www.postgresql.org/download)

5. Create a database
  
  ```zsh
  createdb docmanager
  ```

6. Create a superuser
    
  ```zsh
  python manage.py createsuperuser
  ```

7. Run the server
  
  ```zsh
  python manage.py runserver
  ```

## Deployment

1. [Install the heroku cli](https://devcenter.heroku.com/articles/heroku-cli)
  
  ```zsh
  brew install heroku
  ```

2. Create a new heroku app
  
  ```zsh
  heroku create
  ```

  Copy the url of the app to the clipboard, we will use it later.

  Keep in mind that the app will be created in the directory where you run the command.

3. Add free-tier postgresql db to the app
  
  ```zsh
  heroku addons:create heroku-postgresql:hobby-dev
  ```

4. Configure the environment variables
  
  Point DJANGO_SETTINGS_MODULE to the heroku settings file.
  
  ```zsh
  heroku config:set DJANGO_SETTINGS_MODULE=docmanager.settings.heroku
  ```
  
  Add your secret key
  ```zsh
  heroku config:set SECRET_KEY=<your secret key>
  ```
  
  Paste the url of your api to ALLOWED_HOSTS
  ```zsh
  heroky config:set ALLOWED_HOSTS=<your database url>
  ```

5. Deploy the app and open it in a browser
  
  ```zsh
  git push heroku main && heroku open
  ```
