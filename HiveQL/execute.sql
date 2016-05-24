-- create table tmp as select A.id,A.district_id,C.gap as gap1 from train_y A left outer join (select * from train_y where id = A.id-1 ) C on A.district_id=C.district_id and ;

--create table tmp as select A.id,A.district_id,B.gap as gap1 from train_y A left outer join train_y B on A.district_id=B.district_id and A.id = B.id + 1;

--create table tmp as select (day(o_date)-1)*144+time_slice as id,start_district_id as district_id,sum(gap) as gap from test_order group by o_date,time_slice,start_district_id;

drop table if exists test_x_gap3;
create table test_x_gap3 as select A.id,A.district_id,B.gap as gap
 from test_t A left outer join tmp B
  on A.district_id = B.district_id and A.id = B.id+3;
