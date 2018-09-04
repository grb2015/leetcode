/*
/*
* @Author: Teiei
* @Date:   2018-09-04 16:26:09
* @Last Modified by:   Teiei
* @Last Modified time: 2018-09-04 17:34:35
* https://leetcode-cn.com/problems/employees-earning-more-than-their-managers/description/
* 考察点： 1.自连接join 2.重命名表的巨大作用
* 
遇到的问题：
1.windows下如何执行mysql脚本：
解决方法a：使用Navicat，表-->运行sql文件
解决方法b: mysql -u root -p 之后，在mysql的命令行 source XX.sql 但是如果sql文件用的是utf-8编码,那么
		  好像windows的命令行由于还是gbk编码会出错,这个可以再看一下怎么解决。

2.使用Navicat执行出现下面的错误：
[ERR] 1366 - Incorrect integer value: 'None' for column 'ManagerId' at row 1
显然是这句错了：
insert into Employee_3 (Id, Name, Salary, ManagerId) values ('3', 'Sam', '60000', 'None');
解决方法：None改为NULL(NULL不需要加引号)
*/
drop table Employee_3;
Create table If Not Exists Employee_3 (Id int, Name varchar(255), Salary int, ManagerId int) ;
insert into Employee_3 (Id, Name, Salary, ManagerId) values ('1', 'Joe', '70000', '3');
insert into Employee_3 (Id, Name, Salary, ManagerId) values ('2', 'Henry', '80000', '4');
-- insert into Employee_3 (Id, Name, Salary, ManagerId) values ('3', 'Sam', '60000', 'None');
insert into Employee_3 (Id, Name, Salary, ManagerId) values ('3', 'Sam', '60000', NULL);
insert into Employee_3 (Id, Name, Salary, ManagerId) values ('4', 'Max', '90000', NULL);

SELECT e1.Name  
FROM Employee_3 AS e1, Employee_3 AS e2  /*这里重命名很重要,重命名的运用*/
WHERE e1.ManagerId = e2.Id AND e1.Salary > e2.Salary
-----------------------------------------------------------------

/*
+----------+
| Employee |
+----------+
| Joe      |
+----------+
*/
SELECT e1.Name  as  Employee  /*这里将e1.name这列重命名为Employee,上面的答案中Joe的列名就是Employee*/
FROM Employee AS e1, Employee AS e2  
WHERE e1.ManagerId = e2.Id AND e1.Salary > e2.Salary
