drop table if exists tmp;
create table tmp as select (day(o_date)-1)*144+time_slice as id,start_district_id as district_id,sum(gap) as gap from test_order group by o_date,time_slice,start_district_id;

-------------------------------test_x_gap1----------------------------
--gap1
drop table if exists test_x_gap1;
create table test_x_gap1 as select A.id,A.district_id,B.gap as gap1
 from test_t A left outer join tmp B
  on A.district_id = B.district_id and A.id = B.id+1;


--select count(*) from test_x_gap1;
-- test_x_gap1: 2664，test_t：2838
-- gap1有100多个缺失值，需要填充


-------------------------------test_x_gap2----------------------------
--gap2
drop table if exists test_x_gap2;
create table test_x_gap1 as select A.id,A.district_id,B.gap as gap2
 from test_t A left outer join tmp B
  on A.district_id = B.district_id and A.id = B.id+2;


--select count(*) from test_x_gap2;
-- test_x_gap2: 2636
-- 有些这里需要



-------------------------------test_x_gap3----------------------------
--gap3
drop table if exists test_x_gap3;
create table test_x_gap1 as select A.id,A.district_id,B.gap as gap3
 from test_t A left outer join tmp B
  on A.district_id = B.district_id and A.id = B.id+2;


--  select count(*) from test_x_gap3;
-- test_x_gap1: 2624
-- 有些这里需要

drop table if exists tmp;
