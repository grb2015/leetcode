/*
* @Author: Teiei
* @Date:   2018-09-11 08:31:22
* @Last Modified by:   Teiei
* @Last Modified time: 2018-09-11 09:40:50
* 上升的温度： https://leetcode-cn.com/problems/rising-temperature/description/
* 知识点： 1.自连接(join)
* 		  2.对日期的处理函数 datediff
*/
/*题目：

给定一个 Weather 表，编写一个 SQL 查询，来查找与之前（昨天的）日期相比温度更高的所有日期的 Id。

+---------+------------------+------------------+
| Id(INT) | RecordDate(DATE) | Temperature(INT) |
+---------+------------------+------------------+
|       1 |       2015-01-01 |               10 |
|       2 |       2015-01-02 |               25 |
|       3 |       2015-01-03 |               20 |
|       4 |       2015-01-04 |               30 |
+---------+------------------+------------------+
例如，根据上述给定的 Weather 表格，返回如下 Id:

+----+
| Id |
+----+
|  2 |
|  4 |
+----+
*/
Create table If Not Exists Weather (Id int, RecordDate date, Temperature int);
insert into Weather (Id, RecordDate, Temperature) values ('1', '2015-01-01', '10');
insert into Weather (Id, RecordDate, Temperature) values ('2', '2015-01-02', '25');
insert into Weather (Id, RecordDate, Temperature) values ('3', '2015-01-03', '20');
insert into Weather (Id, RecordDate, Temperature) values ('4', '2015-01-04', '30');

--解答：
-- 跟第6题思想差不多，都是把表一个表用2个别名，然后进行inner join
SELECT * FROM weather as w1,weather as w2 where w1.Temperature > w2.Temperature 
and DATEDIFF(w1.RecordDate,w2.RecordDate) = 1 ;
