# McAstr PA's Backend

This repository contains implementation of backend for my blog post titled 
**"Building an Emotion Aware Response Model through Sentiment Analysis and Information Crowding Architecture"**.

## Installation guide:

1. Create a python Virtual Environment

Run `python -m venv .venv`

2. Activate the virtual environment

> Linux
> 
> `source /.venv/bin/activate`

> Windows
> 
> `/.venv/Scripts/activate`

3. Install all required dependencies

Since Windows and Linux are both had different UVLoop dependency, it is recommended to install the dependency in respective operating system.

> Linux
> 
> `pip install -r requirements.txt`

> Windows
> 
> `pip install -r requirements.windows.txt`

4. Run MySQL database

You can either pull it from Docker and run the instance, or install it from MySQL's official download link.

5. Create `.env` file

The environment variable file used to store credential and secrets value. See `.env.example` file for references. 
Put the `.env` file in the root of project. This is an example for my local `.env` file:

```env
APP_ENV=localhost
APP_DEBUG=true

DATABASE_HOST=localhost
DATABASE_PORT=3306
DATABASE_USER=root
DATABASE_PASSWORD=root
DATABASE_NAME=mcastr_pa_system

SECRET=DYwa7BPn4l74LnalgqYqQTXg3OLSENvc
```

> Warning! SECRET value must be identical to the Vue.JS implementation. 

5. Run database migration

Run it from the root of the project with this command below:

`python /resources/database/migration.py`

6. (Optional) You may want to pre-seed the data if needed.

7. Run FastAPI Dev server

Run the FastAPI dev server from root of the project with command as follow:

`fastapi dev ./src/main.py`

# Contribution

Interested to contribute in this repository? Any questions or feedbacks?

Feel free to email me to yosua_kristianto144@outlook.com