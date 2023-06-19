
-- # of clients subscribed and not subscribed
SELECT [subscribed], count(*) AS total
FROM [bank]
GROUP BY [subscribed];

-- percentage of clients subscribed out of total clients
SELECT CONCAT(CAST(count(*) * 100 / (
SELECT count(*) AS total
FROM [bank]
) AS VARCHAR(2)),"%") AS percentage_of_subscribers
FROM bank
WHERE [subscribed] = 'yes' ;

-- clients subscribed and not subscribed based off of age bracket
SELECT 
CASE WHEN [age] BETWEEN 18 AND 24 THEN '18-24'
WHEN [age] BETWEEN 25 AND 34 THEN '25-34'
WHEN [age] BETWEEN 35 AND 44 THEN '35-44'
WHEN [age] BETWEEN 45 AND 54 THEN '45-54'
WHEN [age] BETWEEN 55 AND 64 THEN '55-64'
WHEN [age] > 64 THEN '65 and older'
END AS age_range,
count(age) AS num_of_subscribers, [subscribed]
FROM [bank]
GROUP BY age_range, [subscribed]
ORDER BY age_range, num_of_subscribers;

-- clients subscribed and not subscribed based on job type
SELECT job, count(*) AS num_of_subscribers, [subscribed] 
FROM [bank]
GROUP BY job,[subscribed] 
ORDER BY num_of_subscribers DESC, [subscribed];

-- clients subscribed and not subscribed based on marital status
SELECT [marital] , count(*) AS num_of_subscribers, [subscribed] 
FROM [bank]
GROUP BY [marital], [subscribed]  
ORDER BY num_of_subscribers DESC;

-- clients subscribed and not subscribed based on education
SELECT [education]  , count(*) AS num_of_subscribers, [subscribed] 
FROM [bank]
GROUP BY [education], [subscribed]  
ORDER BY num_of_subscribers DESC;

-- clients subscribed and not subscribed based on if credit is in default
SELECT [default] , count(*) AS num_of_subscribers, [subscribed] 
FROM [bank]
GROUP BY [default], [subscribed]  
ORDER BY [default], num_of_subscribers DESC;

-- clients subscribed and not subscribed based on yearly balance bracket
SELECT count(*) AS num_of_subscribers, 
CASE WHEN [balance] < 10000 THEN '€10,000 and below'
WHEN [balance] BETWEEN 10000 AND 15000 THEN '€10,000-€15,000'
WHEN [balance] BETWEEN 15000 AND 25000 THEN '€15,000-€25,000'
WHEN [balance] BETWEEN 25000 AND 30000 THEN '€25,000-€30,000'
WHEN [balance] BETWEEN 30000 AND 50000 THEN '€30,000-€50,000'
WHEN [balance] BETWEEN 50000 AND 75000 THEN '€50,000-€75,000'
WHEN [balance] BETWEEN 75000 AND 100000 THEN '€75,000-€100,000'
WHEN [balance] > 100000 THEN '€100,000 and above'
END AS balance_range,
[subscribed]
FROM [bank]
GROUP BY balance_range, [subscribed]
ORDER BY balance_range;

-- clients subscribed and not subscribed based on housing
SELECT [housing] , count(*) AS num_of_subscribers, [subscribed] 
FROM [bank]
GROUP BY [housing], [subscribed]  
ORDER BY [num_of_subscribers] DESC;

-- clients subscribed and not subscribed based on if they have personal loan
SELECT [loan]  , count(*) AS num_of_subscribers, [subscribed] 
FROM [bank]
GROUP BY [loan] , [subscribed]  
ORDER BY num_of_subscribers DESC;

-- clients subscribed and not subscribed based on contact communication type
SELECT [contact]  , count(*) AS num_of_subscribers, [subscribed] 
FROM [bank]
GROUP BY [contact]  , [subscribed]  
ORDER BY [subscribed], num_of_subscribers DESC, [contact] ;

-- clients subscribed and not subscribed based on last month contacted
SELECT [month], count(*) AS num_of_subscribers, [subscribed] 
FROM [bank]
GROUP BY [month], [subscribed] 
ORDER BY [subscribed] DESC, num_of_subscribers

-- top 10 clients subscribed and not subscribed based on month and day contacted

SELECT [month], [day], num_of_subscribers, [subscribed]
FROM (
    SELECT [month], [day], count(*) AS num_of_subscribers, [subscribed]
    FROM [bank]
    GROUP BY [month], [day], [subscribed]
    ORDER BY [subscribed] DESC, num_of_subscribers DESC
    LIMIT 10
) AS query1

UNION ALL

SELECT [month], [day], num_of_subscribers, [subscribed]
FROM (
    SELECT [month], [day], count(*) AS num_of_subscribers, [subscribed]
    FROM [bank]
    GROUP BY [month], [day], [subscribed]
    ORDER BY [subscribed], num_of_subscribers DESC
    LIMIT 10
) AS query2;

-- clients subscribed and not subscribed based on duration (seconds) of contact
SELECT [duration] , count(*) AS num_of_subscribers, [subscribed] 
FROM [bank]
GROUP BY [duration] , [subscribed] 
ORDER BY [subscribed] DESC, num_of_subscribers DESC;

-- clients subscribed and not subscribed based on # of contacts during this campaign
SELECT [campaign]  , count(*) AS num_of_subscribers, [subscribed] 
FROM [bank]
GROUP BY [campaign]  , [subscribed]
ORDER BY [subscribed] DESC ,num_of_subscribers DESC;

-- clients subscribed and not subscribed based on pdays (number of days that passed by after the client was last contacted)
SELECT DISTINCT[pdays], CASE WHEN [pdays]=-1 THEN "Not Previously Contacted" ELSE "Contacted"END AS label,
count(*) AS num_of_subscribers, [subscribed] 
FROM [bank]
GROUP BY [subscribed], [pdays]
ORDER BY num_of_subscribers DESC;

-- clients subscribed and not subscribed based on previous (# of contacts before this campaign)
SELECT [previous] , count(*) AS num_of_subscribers, [subscribed]
FROM [bank]
GROUP BY [previous], [subscribed]  
ORDER BY [subscribed] DESC, num_of_subscribers DESC ;

-- clients subscribed and not subscribed based on poutcome (outcome of the previous marketing campaign) 
SELECT [poutcome], count(*) AS num_of_subscribers, [subscribed]
FROM [bank]
GROUP BY [poutcome], [subscribed] 
ORDER BY [subscribed] DESC, num_of_subscribers DESC;
