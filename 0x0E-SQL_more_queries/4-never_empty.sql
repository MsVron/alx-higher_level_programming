-- This script establishes the id_not_null table on your MySQL server.

-- Create the table id_not_null, setting a default id value of 1.
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
