#!/bin/bash

shopt -s expand_aliases
alias psql='docker exec -it gc_postgres psql -Upostgres'  # use psql from docker

psqluser="postgres"     # Database username
psqlpass="postgres"     # Database password
psqldb="bxdoan_falcon"  # Database name

function create_and_seed {
    # Create database postgres
    echo "Create database postgres"
    psql -c "CREATE DATABASE $psqldb;"

    # Create the customers table
    echo "Create the customer table"
    psql -d $psqldb -c "DROP TABLE IF EXISTS customer;
                                      CREATE TABLE customer(id serial PRIMARY KEY,
                                               name text,
                                               dob date,
                                               updated_at timestamp);"

    # Insert some seeding data customers
    echo "Insert some seeding data customer"
    psql -d $psqldb -c "INSERT INTO customer (name, dob, updated_at) VALUES
        ('Ronaldo', '1/8/1991', '2019-08-22 04:05:01'),
        ('Messi', '3/4/1992', '2019-08-22 04:05:02'),
        ('Modric', '3/28/1993', '2019-08-22 04:05:03'),
        ('Salah', '4/25/1994', '2019-08-22 04:05:04'),
        ('Pogba', '1/8/1995', '2019-08-22 04:05:05'),
        ('Kante', '1/22/1996', '2019-08-22 04:05:06'),
        ('Neymar', '1/23/1997', '2019-08-22 04:05:07'),
        ('Mbappe', '1/13/1998', '2019-08-22 04:05:08'),
        ('Kroos', '1/11/1999', '2019-08-22 04:05:09'),
        ('Oezil', '1/10/1990', '2019-08-22 04:05:010');"

    # Create the users table
    echo "Create the users table"
    psql -d $psqldb -c "DROP TABLE IF EXISTS users;
                              CREATE TABLE users(id serial PRIMARY KEY,
                                       username text,
                                       password text,
                                       dob date);"

     # Insert some seeding data users
     echo "Insert some seeding data users"
     psql -d $psqldb -c "INSERT INTO users (username, password, dob) VALUES
     		                               ('doan', '\$pbkdf2-sha256\$29000\$4rz3HuN8zxlDaC1lLAVASA\$l9uzGvo1fwyO9xSIElk8OjvydIvFKCy3Vnd1KzfJWF8', '1/10/1990');"

    # Show customers table
    psql -d $psqldb -c "SELECT * FROM customer;"
}

die() {
    echo "$@" >&2
    exit 1
}

if psql -Upostgres -lqt -P pager=off | cut -d'|' -f1 | grep -qw $psqluser; then  # if user exists
    # database exists
    echo "The database postgres exist. Drop it!"
    psql -c "DROP DATABASE if exists $psqldb;"
    create_and_seed
fi
