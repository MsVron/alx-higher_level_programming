-- This script retrieves a list of all cities in California
-- that are stored in the hbtn_0d_usa database.

-- Utilizing subqueries and the '=' comparison operator to extract data.
SELECT cities.id, cities.name
FROM cities
WHERE state_id = (
    SELECT states.id
    FROM states
    WHERE states.name = 'California'
);
