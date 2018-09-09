/*
# -*- coding: utf-8 -*-
# @Author: Teiei
# @Date:   2018-09-09 17:39:00
# @Last Modified by:   Teiei
# @Last Modified time: 2018-09-09 17:39:00
# 知识点：这道题其实是让我们对一个表进行交集，并集等。
#  可以使用IN / NOT IN
*/
Create table If Not Exists Customers (Id int, Name varchar(255));
Create table If Not Exists Orders (Id int, CustomerId int);
-- Truncate table Customers
insert into Customers (Id, Name) values ('1', 'Joe');
insert into Customers (Id, Name) values ('2', 'Henry');
insert into Customers (Id, Name) values ('3', 'Sam');
insert into Customers (Id, Name) values ('4', 'Max');
-- Truncate table Orders
insert into Orders (Id, CustomerId) values ('1', '3');
insert into Orders (Id, CustomerId) values ('2', '1');



-- 解答1 
SELECT Name AS Customers FROM Customers 
WHERE Id NOT IN (SELECT CustomerId FROM Orders);
