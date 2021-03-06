#https://leetcode-cn.com/problems/second-highest-salary/description/
# 知识点： distinct/null的处理
# 返回第二高的薪水。如果不存在第二高的薪水，那么查询应返回 null。

# issue1: 没有正确处理null的情况
# issue2：没有考虑到重复薪资的情况，比如最高薪资有多个。

#create table Employee(Id int ,Salary int);
#insert into  Employee(Id,Salary) values('1','100');
#insert into  Employee(Id,Salary) values(3,300);
#insert into  Employee(Id,Salary) values('1','100');

#select * from Employee ORDER BY Salary desc LIMIT 1,1;
#select Salary as SecondHighestSalary  from Employee ORDER BY Salary desc LIMIT 1,1;
--另一种as的用法
#select (select Salary  from Employee ORDER BY Salary desc LIMIT 1,1 )as SecondHighestSalary ;

-- version2 :使用Distinct来处理重复的Salary,使用IFNULL函数来处理空
select IFNULL((select Distinct Salary from Employee order by Salary DESC limit 1,1),null)
as SecondHighestSalary
