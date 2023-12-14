-- AUTHOR: Samuella M. Aglago
-- Group records by same scores

SELECT score, COUNT(*) AS number 
FROM second_table
GROUP BY score
ORDER BY number DESC;
