# Challenge Set 9
## Part I: W3Schools SQL Lab 

*Introductory level SQL*

This challenge uses the [W3Schools SQL playground](http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all). Please add solutions to this markdown file and submit.

1. Which customers are from the UK? 

    1. | CustomerName          | Country |
        | :-------------------- | :------ |
        | Around the Horn       | UK      |
        | B's Beverages         | UK      |
        | Consolidated Holdings | UK      |
        | Eastern Connection    | UK      |
        | Island Trading        | UK      |
        | North/South           | UK      |
        | Seven Seas Imports    | UK      |

    2. ```
        SELECT CustomerName, Country FROM Customers WHERE country = 'UK';
        ```

2. What is the name of the customer who has the most orders?
    1. | CustomerName | COUNT(*) |
        | :----------- | :------- |
        | Ernst Handel | 10       |

3. ```
    SELECT CustomerName, COUNT(*) FROM Customers INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID GROUP by CustomerName, Customers.CustomerID ORDER BY COUNT(*) DESC LIMIT 1;
    ```

3. Which supplier has the highest average product price?

1. | SupplierName               | AVG_PRICE |
    | :------------------------- | :-------- |
    | Aux joyeux ecclésiastiques | 140.75    |

    ```
    SELECT SupplierName, avg(Price) as AVG_PRICE FROM Suppliers INNER JOIN Products ON Suppliers.SupplierID = Products.SupplierID GROUP BY Suppliers.SupplierID ORDER BY avg(Price) DESC LIMIT 1;
    ```

4.How many different countries are all the customers from? (*Hint:* consider [DISTINCT](http://www.w3schools.com/sql/sql_distinct.asp).)

| Count |
| :---- |
| 21    |

```
SELECT COUNT(Distinct(Country)) AS Count From Customers;
```

5. What category appears in the most orders?

| CategoryName   | COUNT(*) |
| :------------- | :------- |
| Dairy Products | 19600    |

```
SELECT c.CategoryName, COUNT(*) FROM Orders o INNER JOIN OrderDetails od  INNER JOIN Products p ON od.ProductID = p.ProductID INNER JOIN Categories c ON p.CategoryID = c.CategoryID GROUP BY c.CategoryName ORDER BY COUNT(*) DESC LIMIT 1;
```

6. What was the total cost for each order?

    | OrderID | sum(p.Price) |
    | :------ | :----------- |
    | 10248   | 69.8         |
    | 10249   | 76.25        |
    | 10250   | 83.7         |
    | 10251   | 61.55        |
    | 10252   | 117.5        |

    ```
    SELECT o.OrderID, sum(od.Quantity * p.Price)  FROM Orders o INNER JOIN OrderDetails od ON o.OrderID = od.OrderID INNER JOIN Products p ON od.ProductID = p.ProductID GROUP BY o.OrderID LIMIT 10;
    ```

7. Which employee made the most sales (by total price)?

| FirstName | LastName | TOTAL_PRICE |
| :-------- | :------- | :---------- |
| Steven    | Buchanan | 15353.6     |

```
SELECT e.FirstName, e.LastName, sum(od.Quantity * p.Price) as TOTAL_PRICE  FROM Orders o INNER JOIN OrderDetails od ON o.OrderID = od.OrderID INNER JOIN Products p ON od.ProductID = p.ProductID INNER JOIN Employees e ON o.EmployeeID = e.EmployeeID GROUP BY o.OrderID ORDER BY sum(od.Quantity * p.Price) DESC LIMIT 1;
```

8. Which employees have BS degrees? (*Hint:* look at the [LIKE](http://www.w3schools.com/sql/sql_like.asp) operator.)

| FirstName | LastName  |
| :-------- | :-------- |
| Janet     | Leverling |
| Steven    | Buchanan  |

```
SELECT FirstName, LastName FROM [Employees] WHERE Notes like '%BS%'
```

9. Which supplier of three or more products has the highest average product price? (*Hint:* look at the [HAVING](http://www.w3schools.com/sql/sql_having.asp) operator.)

| SupplierName  | SupplierID | avg(p.Price) |
| :------------ | :--------- | :----------- |
| Tokyo Traders | 4          | 46           |

```
SELECT s.SupplierName, p.SupplierID, avg(p.Price) FROM Products p INNER JOIN Suppliers s ON p.SupplierID = s.SupplierID WHERE p.SupplierID in (SELECT SupplierID FROM Products GROUP BY SupplierID HAVING COUNT(*) >= 3) GROUP BY s.SupplierName, p.SupplierID ORDER BY avg(p.Price) DESC LIMIT 1;
```

