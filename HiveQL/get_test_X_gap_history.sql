
-------------------------test_x_gap_average----------------------------------------------------
drop table if exists tmp_x;
create table tmp_x
as 
select B.id,B.district_id, avg(A.gap) as gap_avg
--select B.*,A.*
from test_t B left join  train_y A on (A.district_id=B.district_id) 
where (B.id-A.id) % (7*144)=0
group by B.id,B.district_id;
--limit 10;

select count(*),sum(case when gap_avg is null then 1 else 0 end) from tmp_x;
-- test_t: 2838, test_x_gap_average: 2769



drop table if exists test_x_gap_average;
create table test_x_gap_average
as select A.id,A.district_id,
--select A.*,B.*,
case
when isnull(B.gap_avg) then 0
else B.gap_avg
end
as gap_avg
from test_t A left join tmp_x B
on (A.district_id=B.district_id and A.id=B.id)
;
--
select count(*),sum(case when gap_avg is null then 1 else 0 end) from test_x_gap_average;
--2838,0
drop table tmp_x;




-------------------------test_x_gap_latest----------------------------------------------------
drop table if exists tmp_x;
create table tmp_x
as 
select B.id,B.district_id,A.gap as gap_latest
--select B.*,A.*
from test_t B left join  train_y A on A.district_id=B.district_id 
and B.id= A.id + 144*7
;
--limit 10;

--
select count(*),sum(case when gap_latest is null then 1 else 0 end) from tmp_x;
--2838,755个空，需要填充


create table test_x_gap_latest
as
select A.id,A.district_id,
(case when A.gap_latest is null then B.gap_avg else A.gap_latest end) as gap_latest
from tmp_x A left join test_x_gap_average B on A.id=B.id and A.district_id=B.district_id
;

select count(*),sum(case when gap_latest is null then 1 else 0 end) from test_x_gap_latest;
--2838,0

drop table tmp_x;



