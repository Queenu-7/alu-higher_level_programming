-- Script that lists score and name, excluding rows where name is NULL or empty, ordered by score descending
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
