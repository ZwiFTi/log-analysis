# Python Log Analysis Project

## Table of Contents

* [Description](#description)
* [Installation](#installation)
* [JSON Endpoints](#REST)
* [Contributing](#contributing)
* [Known issues](#known)
* [License](#known)

## Description

This is a Udacity fullstack nanodegree project. We have to build a Python application
that logs output to questions regarding a .sql database. The sql database in question
is `newsdata.sql`, a database which contains newspaper articles, as well as a web server
log. 

Our log program should answer the following questions using SQL queries:

- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

## Installation

1. Make sure you have Vagrant & VirtualBox installed
2. Make sure you have the Udacity repo
`git clone https://github.com/udacity/fullstack-nanodegree-vm.git`
3. [Download](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and place `newsdata.sql` into the `/vagrant` folder
4. cd into the vagrant directory, then:

**In terminal:**

a) Get project and load up vagrant

    git clone https://github.com/ZwiFTi/log-analysis.git
    vagrant up && vagrant ssh
    cd /vagrant/log-analysis/
    
b) Populate the sql data with

    psql -d news -f newsdata.sql
    
c) Connect to the db

    psql -d news
    
d) Create views required for the project

```
CREATE VIEW view_error_percent AS 
SELECT date(log.time),
       ROUND(100.0 * COUNT(*) FILTER (WHERE log.status NOT LIKE '%200%') / COUNT(*),2) AS error_percent
  FROM log
 GROUP BY date(log.time);
```

5. Run program for query results

       python log-analysis.py
    


## Contributing

This project is a practice project, and is therefore not open for contribution.


## Known issues

There is no known issues to date.


## License

The contents of this repository are covered under the [MIT License](LICENSE).





