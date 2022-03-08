-- Lists the number of records with the same score in second_table of hbtn_0c_0 in MySQL server
SELECT score, COUNT(score) as number
FROM second_table
GROUP BY score
ORDER BY score DESC;
