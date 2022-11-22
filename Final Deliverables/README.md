# Setup Guide

We are live at: http://159.122.178.236:31098/

Demo video link : https://www.loom.com/share/117c36a1fa1344828258e0187eccea95

## Backend - Local

### Move to the backend directory

```sh
cd Final\ Deliverables/backend
```

### Create virtual environment

```sh
python3 -m venv venv
```

### Activate virtual environment

```sh
. venv/bin/activate
```

### Install dependencies

```sh
pip install -r requirements.txt
```

### Setup environment variables

```sh
touch .env
```
Create necessary values in the `.env` file by referencing the `.env.template` file.

### Run

```sh
flask run
```

### Additional

```sh
flask create-db
```
To create some data in the DB for development purposes.

## Frontend - Local

### Move to the frontend directory

```sh
cd Final\ Deliverables/frontend
```

### Install dependencies

```sh
npm install
```

### Run

```sh
npm start
```

