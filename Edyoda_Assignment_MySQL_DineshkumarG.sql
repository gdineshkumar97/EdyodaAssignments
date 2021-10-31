-- NAME 		: Dineshkumar G
-- Assignement 	: MySQL
-- Instructor	: Bharati Reddy
-- Batch		: DS14082021

CREATE DATABASE edyoda;

USE edyoda;

-- Creating SalesPeople Table
CREATE TABLE SalesPeople(
	Snum SMALLINT,
	Sname VARCHAR(20) NOT NULL,
    City VARCHAR(20) NOT NULL,
    Comm SMALLINT,
    PRIMARY KEY(Snum)
	);

-- Inserting values into SalesPeople	
INSERT INTO SalesPeople (`Snum`, `Sname`, `City`, `Comm`) VALUES
	(1001, 'Peel', 'London', 12),
	(1002, 'Serres', 'Sanjose', 13),
	(1003, 'Axelrod', 'Newyork', 10),
	(1004, 'Motika', 'London', 11),
	(1007, 'Rifkin', 'Barcelona', 15);

-- Creating Customers Table
CREATE TABLE Customers (
	Cnum SMALLINT NOT NULL,
	Cname varchar(60) DEFAULT NULL,
	City varchar(60) NOT NULL,
	Snum SMALLINT DEFAULT NULL
	);

-- Inserting values into customers
INSERT INTO Customers (`Cnum`, `Cname`, `City`, `Snum`) VALUES
	(2001, 'Hoffman', 'London', 1001),
	(2002, 'Giovanni', 'Rome', 1003),
	(2003, 'Liu', 'Sanjose', 1002),
	(2004, 'Grass', 'Berlin', 1002),
	(2006, 'Clemens', 'London', 1001),
	(2007, 'Pereira', 'Rome', 1004),
	(2008, 'Cisneros', 'Sanjose', 1007);

-- Creating orders table
CREATE TABLE Orders (
	Onum SMALLINT NOT NULL,
	Amt float DEFAULT NULL,
	Odate date DEFAULT NULL,
	Cnum SMALLINT DEFAULT NULL,
	Snum SMALLINT DEFAULT NULL
	);
-- Inserting values into orders table
INSERT INTO Orders (`Onum`, `Amt`, `Odate`, `Cnum`, `Snum`) VALUES
	(3001, 18.69, '1990-10-03', 2008, 1007),
	(3002, 1900.1, '1990-10-03', 2007, 1004),
	(3003, 767.19, '1990-10-03', 2001, 1001),
	(3005, 5160.45, '1990-10-03', 2003, 1002),
	(3006, 1098.16, '1990-10-03', 2008, 1007),
	(3007, 75.75, '1990-10-04', 2004, 1002),
	(3008, 4273, '1990-10-05', 2006, 1001),
	(3009, 1713.23, '1990-10-04', 2002, 1003),
	(3010, 1309.95, '1990-10-06', 2004, 1002),
	(3011, 9891.88, '1990-10-06', 2006, 1001);

-- Display salespeople,customers,orders table
SELECT * FROM salespeople;
SELECT * FROM Customers;
SELECT * FROM Orders;

-- Adding PRIMARY key
ALTER TABLE Customers
	ADD PRIMARY KEY (`Cnum`),
	ADD KEY `Snum` (`Snum`);

-- Adding PRIMARY key
ALTER TABLE Orders
	ADD PRIMARY KEY (`Onum`),
	ADD KEY `Cnum` (`Cnum`),
	ADD KEY `Snum` (`Snum`);

-- Adding UNIQUE key
ALTER TABLE SalesPeople
	ADD UNIQUE KEY `Sname` (`Sname`);

-- Adding FOREIGN KEY
ALTER TABLE Customers
	ADD CONSTRAINT `customers_ibfk_1` FOREIGN KEY (`Snum`) REFERENCES `salespeople` (`Snum`);

-- Adding FOREIGN KEY
ALTER TABLE Orders
	ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`Cnum`) REFERENCES `customers` (`Cnum`),
	ADD CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`Snum`) REFERENCES `salespeople` (`Snum`);


-- 1) Count the number of Salesperson whose name begin with ‘a’/’A’

SELECT COUNT(*) FROM SalesPeople
WHERE Sname LIKE 'a%' OR Sname LIKE 'A%';

-- 2)Display all the Salesperson whose all orders worth is more than Rs. 2000.

SELECT COUNT(*)
FROM salespeople INNER JOIN orders on salespeople.Snum = orders.Snum WHERE Amt > 2000;


-- 3)Count the number of Salesperson belonging to Newyork.

SELECT COUNT(*) FROM salespeople
WHERE city = 'NewYork';

-- 4) Display the number of Salespeople belonging to London and belonging to Paris.

SELECT COUNT(*) FROM Salespeople
WHERE City = 'London';

SELECT COUNT(*) FROM Salespeople
WHERE City = 'Paris';


	
-- 5)Display the number of orders taken by each Salesperson and their date of orders.

SELECT salespeople.Sname, 
	orders.Odate 
	FROM salespeople 
	INNER JOIN orders ON salespeople.Snum = orders.Snum;