-- Retrieves the average temperature (in Fahrenheit)
-- for each city, sorted in descending order of temperature.
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
