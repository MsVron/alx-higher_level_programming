-- This script generates the unique_id table on your MySQL server.

-- Create the unique_id table with a unique id constraint and a default value of 1.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
