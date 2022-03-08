-- Lists all records of second_table of hbtn_0c_0 in MySQL server
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
