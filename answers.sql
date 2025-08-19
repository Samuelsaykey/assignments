-- Select the salesDB database to use for subsequent queries
USE salesDB;
-- Show all tables available in the current database
SHOW TABLES;
-- Select a random employeeNumber from employees table where jobtitle is 'Sales Rep'
SELECT 
    employeeNumber
FROM
    employees
WHERE
    jobtitle = 'Sales Rep'
ORDER BY RAND()
LIMIT 1;

-- question 1: Retrieve checkNumber, paymentDate, and amount from the payments table
SELECT checkNumber, paymentDate, amount
FROM payments;

-- question 2: Get orderDate, requiredDate, and status for orders that are 'In Process', sorted by orderDate (latest first)
SELECT orderDate, requiredDate, status
FROM orders
WHERE status = 'In Process'
ORDER BY orderDate DESC;

-- question 3: Get firstName, lastName, and email of employees with jobTitle 'Sales Rep', sorted by employeeNumber descending
SELECT firstName, lastName, email
FROM employees
WHERE jobTitle = 'Sales Rep'
ORDER BY employeeNumber DESC;

-- question 4: Retrieve all columns and records from the offices table
SELECT *
FROM offices;

-- question 5: Get productName and quantityInStock for 5 products with the lowest buyPrice
SELECT productName, quantityInStock
FROM products
ORDER BY buyPrice ASC
LIMIT 5;