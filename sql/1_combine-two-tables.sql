/*
* @Author: Teiei
* @Date:   2018-09-04 07:52:35
* @Last Modified by:   Teiei
* @Last Modified time: 2018-09-04 08:16:00
* https://leetcode-cn.com/problems/combine-two-tables/description/
*/
create table Person (PersonId int, FirstName varchar(255), LastName varchar(255))
Create table Address (AddressId int, PersonId int, City varchar(255), State varchar(255))
insert into Person (PersonId, LastName, FirstName) values ('1', 'Wang', 'Allen')
insert into Address (AddressId, PersonId, City, State) values ('1', '2', 'New York City', 'New York')

--以Person为基准进行连接即可
select FirstName, LastName, City, State from Person left join Address on Person.PersonId = Address.PersonId;
-- 可以通过如下查看生成的表,增加理解
select * from Person left join Address on Person.PersonId = Address.PersonId;