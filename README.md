<p align="center>
	<h2 align="center"> Personal Finance Tracker </h2>
	<h4> API for the finance tracker backend task for Fischer Jordan <h4>
</p>

## Table of Contents
- [Key Features](#key-features)
  - [Users](#users)
  - [Transactions](#transaction)
  - [Dashboard](#dashboards)
  - [Generate Report](#report)
  - [Split Expenses](#split)

- [Usage](#usage)
  - [Spin up docker containers](#spin-up-all-the-containers)
  - [Migrate database changes](#migrate-the-database)
  - [Create superuser](#create-superuser)
  - [View logs](#view-logs)
    
- [API Documentation](#api-documentation)
- [Developer](#developer)

<br>

## Key Features
### Users
- [x] Custom User Model
- [x] JWT based user authentication
### Transactions
- [x] CRUD for transactions
- [x] Create categories for income and expense
- [x] Set budgets for categories
### Dashboard
- [x] Get income vs expense querysets
- [x] Get category vs budget querysets
### Generate Report
- [x] Generate a csv file of transaction data
### Split Expenses
- [x] Split expenses with other users
- [x] Settle expenses
- [x] View all split expenses

## Usage

### Spin up all the containers
```bash
docker compose -f docker-compose.local.yml up -d --build
```

### Migrate the database
```bash
docker compose -f docker-compose.local.yml run djangi python manage.py migrate
```

### Create super user
```bash
docker compose -f docker-compose.local.yml run djangi python manage.py createsuperuser
```

## View Logs
```bash
docker compose logs <container-name>
```

## API Documentation
Postman API Documentations - [Finance Tracker ](https://documenter.getpostman.com/view/28843543/2sA3QpAssY)

## Developer
<h4>Aarabi Balakrishnan </h4>
<a href = "github.com/rb-25/"> Github </a> <br>
<a href = https://www.linkedin.com/in/aarabi-balakrishnan-88629b28a/"> LinkedIn </a>
  
