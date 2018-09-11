/*
* @Author: Teiei
* @Date:   2018-09-10 09:47:42
* @Last Modified by:   Teiei
* @Last Modified time: 2018-09-11 09:11:40
*  删除重复的电子邮箱 ：https://leetcode-cn.com/problems/delete-duplicate-emails/description/
*  知识点：删除重复的记录.
*  		> delete删除多表和单表的格式 https://dev.mysql.com/doc/refman/8.0/en/delete.html
*/
create TABLE person6 (id int ,email varchar(255));
insert into  person6(id,email)values('1','john@example.com');
insert into  person6(id,email)values('2','bob@example.com');
insert into  person6(id,email)values('3','john@example.com');

-- 解决方法 1
DELETE p2 FROM Person6  p1, Person6  p2 WHERE p1.Email = p2.Email AND p2.Id > p1.Id;
--等价于
DELETE p2 FROM Person p1 JOIN Person p2 
ON p2.Email = p1.Email WHERE p2.Id > p1.Id;
-- 这里的JOIN其实就是INNER JOIN，INNER可以省略

/* 
解释：
1.DELETE p2 FROM 意思是从p2中删除符合后面条件的元素，也可以DELETE p1, p2 FROM
 总之from之前的table都会删除。
2. as可以省略 
3.可以参考下面2个结果来帮助理解：
select *  FROM Person6  p1, Person6  p2 WHERE p1.Email = p2.Email AND p2.Id > p1.Id ;
select *  FROM Person6 as p1, Person6 as p2 WHERE p1.Email = p2.Email ;

拓展：
上面给了2个表(FROM Person6  p1, Person6  p2 )，其实是一种内连接：
等同于
DELETE p2 FROM Person p1 JOIN Person p2 
ON p2.Email = p1.Email WHERE p2.Id > p1.Id;

关于join可参考
https://github.com/grb2015/sql/blob/master/12-join.sql  // 内连接
https://github.com/grb2015/sql/blob/master/13_advance_join.sql  // 外连接(left join ,right join)

*/


-- 解决方法2：
-- 先找出重复邮箱的，再删除
-- http://www.cnblogs.com/grandyang/p/5371227.html?spm=a2c4e.11153940.blogcont341594.4.34ea7058pIkuf4
--我们可以按照邮箱群组起来，然后用Min关键字挑出较小的
DELETE FROM Person WHERE Id NOT 
IN (SELECT Id FROM (SELECT MIN(Id) Id FROM Person GROUP BY Email) p);

/* 解释：
1.这个必须加上MIN(ID)
SELECT MIN(Id) Id FROM Person GROUP BY Email;
不然得话如下情况：
ID  EMAIL 
2	bob@example.com
3	john@example.com
1	john@example.com
通过 不加MIN 即：SELECT Id FROM Person GROUP BY Email;
得到的是
ID
2
3
不正确。
但是如果我先对id进行排序，再SELECT  Id FROM Person GROUP BY Email;应该就可以了
错！即便是先排序也是不行的：
create view p1  as select *from person6 order by id  ;  
SELECT *from p1 GROUP BY email;
这样查出来仍然是：
2	bob@example.com
3	john@example.com


2. DELETE FROM Person6 WHERE Id NOT IN (SELECT MIN(Id) Id FROM Person6 GROUP BY Email );
这种查询看起来可以了，但是会报错。
所以还要再包装一层SELECT as  ,这里p应该是as p：
DELETE FROM Person6 WHERE Id NOT IN 
(SELECT Id FROM (SELECT MIN(Id) Id FROM Person6 GROUP BY Email) p);
*/