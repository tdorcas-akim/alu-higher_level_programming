-- This script updates the score of Bob to 10 in the second_table
-- We are identifying Bob using the name field and not using his id

UPDATE second_table
SET score = 10
WHERE name = 'Bob';
