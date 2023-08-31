-- This script displays a list of all cities stored in the hbtn_0d_usa database.

-- Utilizing a join operation to present specific data.
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
ON cities.state_id = states.id;
