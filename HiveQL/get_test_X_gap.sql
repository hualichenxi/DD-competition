-------------------------------test_x_gap1----------------------------
--gap1
create table test_x_gap1 as select A.id,A.district_id,sum(B.gap)
 from test_t A left join test_order B
  on A.district_id = B.start_district_id where (A.id - ((day(B.o_date)-1)*144+B.time_slice))=1 
  group by A.id,A.district_id;

--select count(*) from test_x_gap1;
-- test_x_gap1: 2664，test_t：2838
-- gap1有100多个缺失值，需要填充


-------------------------------test_x_gap2----------------------------
--gap1
create table test_x_gap2 as select A.id,A.district_id,sum(B.gap)
 from test_t A left join test_order B
  on A.district_id = B.start_district_id where (A.id - ((day(B.o_date)-1)*144+B.time_slice))=2
  group by A.id,A.district_id;
select count(*) from test_x_gap2;
-- test_x_gap2: 2636
-- 有些这里需要



-------------------------------test_x_gap3----------------------------
--gap1
create table test_x_gap3 as select A.id,A.district_id,sum(B.gap)
 from test_t A left join test_order B
  on A.district_id = B.start_district_id where (A.id - ((day(B.o_date)-1)*144+B.time_slice))=3
  group by A.id,A.district_id;

  select count(*) from test_x_gap3;
-- test_x_gap1: 2624
-- 有些这里需要
