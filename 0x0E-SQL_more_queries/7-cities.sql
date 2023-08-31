-- This script establishes the hbtn_0d_usa database and creates the cities table within it on your MySQL server.

-- Create the hbtn_0d_usa database if it doesn't exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to/use the hbtn_0d_usa database.
USE hbtn_0d_usa;

-- Create the cities table with auto-incremented id, state_id as a foreign key, and other fields.
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id) ON DELETE CASCADE
);
