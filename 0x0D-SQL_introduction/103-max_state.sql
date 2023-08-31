-- Shows the maximum temperature recorded in each state,
-- sorted alphabetically by state name.
SELECT state, MAX(value) AS max_temp 
FROM temperatures
GROUP BY state
ORDER BY state;
