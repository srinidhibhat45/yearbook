# Yearbook
<!-- Heads -->
  <p align="center">
    <br />
    <br />
    <br />
    <a href="https://sushiksha-yearbook.herokuapp.com/"target="_blank" rel="noopener noreferrer">View a Live Demo</a>
    · 
    <a href="https://github.com/srinidhibhat45/yearbook/issues/new">Report a Bug</a>
    ·
    <a href="https://github.com/srinidhibhat45/yearbook/issues/new">Request a Feature</a>
  </p>

<!-- Logos -->
<br>
<p align="center">
  <a href="https://github.com/kan12340987/Tejas-SCL-maxo/blob/main/README.md">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/768px-Python-logo-notext.svg.png" alt="Logo" width="80" height="80"> &nbsp;
    <a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangopowered126x54.gif" border="0" alt="Powered by Django." title="Powered by Django." /></a>  
    <img src="https://getbootstrap.com/docs/5.0/assets/brand/bootstrap-logo-shadow.png" alt="Bootstrap logo" width="100" height="80">  
  </a>
<br>
<br>

<!-- Repo detail Stickers -->
<p align="center">                          
    <a href="https://github.com/srinidhibhat45/yearbook/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/srinidhibhat45/yearbook?style=for-the-badge"></a>
    <a href="https://github.com/srinidhibhat45/yearbook/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/srinidhibhat45/yearbook?style=for-the-badge"></a>
    <a href="https://github.com/srinidhibhat45/yearbook/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/srinidhibhat45/yearbook?style=for-the-badge"></a>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#project-description">Project Description</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#development">Development</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing / Adding features</a></li>
  </ol>
</details>

<br />

<!-- About Project -->

## About the Project

#### Project Description

1. Backend Framework: **Django**
2. Front-end Framework: **Bootstrap**
3. Database used: **Sqlite**

<!-- Getting started -->

## Getting Started

### Installation 

1. Fork and Clone
    <ol>
    <li>Fork the **Yearbook** Repository</li>
    <li>Clone the repo to your local system.</li>
    </ol>

2. Create a Virtual Environment for the Project

    In Windows
    ```bash
    pip install virtualenv
    virtualenv venv
    venv\Scripts\activate
    ```

    In Ubuntu/MacOS
    ```bash
    python -m virtualenv venv

    source venv/bin/activate
    ```
   
   If you are using another name for the virtual environment other than `venv`, then please mention it in `.gitignore`.

3. Install all the requirements

    ```bash
    pip install -r requirements.txt
    ```
### Development

4. Checkout to a different branch
     ```git
    git status
    git pull
    git branch
    git checkout -b <your-branch-here>
   
   ```
5. Make migrations/ Create db.sqlite3

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Create a super user.
    In Django, if you want to access admin page, you need to create an account with staff status first.
    ```djangotemplate
    python manage.py createsuperuser
    ```
   Then select your username and password. You can bypass a common password for development purposes.
   
7. Run the server on localhost:
    ```bash
    python manage.py runserver
    ```

8. Make the changes and send a PR, referencing the changes.
   

## Contributing
   Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change in the project.

<br>
