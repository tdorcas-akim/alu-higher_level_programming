-- This script lists all records from the second_table in the database
-- The results display both the score and the name, ordered by top score first

SELECT score, name
FROM second_table
ORDER BY score DESC;
