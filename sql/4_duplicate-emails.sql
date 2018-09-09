/*
# -*- coding: utf-8 -*-
# @Author: Teiei
# @Date:   2018-09-09 17:01:20
# @Last Modified by:   Teiei
# @Last Modified time: 2018-09-09 17:01:20
# https://leetcode-cn.com/problems/duplicate-emails/description/
# 知识点： group by  /having 
*/
Create table If Not Exists Person1 (Id int, Email varchar(255));
Truncate table Person1 
insert into Person1 (Id, Email) values ('1', 'a@b.com');
insert into Person1 (Id, Email) values ('2', 'c@d.com');
insert into Person1 (Id, Email) values ('3', 'a@b.com');

-- 解答：
select * from Person1 group by Email having count(email)>1;