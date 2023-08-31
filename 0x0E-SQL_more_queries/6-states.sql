-- This script establishes the hbtn_0d_usa database and the states table within it on your MySQL server.

-- Create the hbtn_0d_usa database if it doesn't exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to/use the hbtn_0d_usa database.
USE hbtn_0d_usa;

-- Create the states table with an auto-incremented id as the primary key.
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT,
    name VARCHAR(256),
    PRIMARY KEY (id)
);
