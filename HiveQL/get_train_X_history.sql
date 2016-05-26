-------------------------train_x_gap_average----------------------------------------------------
--where DATEDIFF(B.o_date,A.o_date) % 7 =0 and B.time_slice=A.time_slice
drop table if exists x_tmp;
create table x_tmp
as 
select B.id,B.district_id, avg(A.gap) as gap_avg
--select B.*,A.*
from train_y B left join  train_y A on (A.district_id=B.district_id)
-- and ( B.id= A.id + 144*7 or B.id= A.id + 144*7 )
where (B.id-A.id) % (7*144)=0
group by B.id,B.district_id;
--limit 10;

select count(*),sum(case when gap_avg is null then 1 else 0 end) from x_tmp;
--163491,空的纪录为0个,且163491和原始train_y的个数相同，不需要再做链接
alter table x_tmp rename to train_x_gap_average;




-------------------------train_x_gap_latest----------------------------------------------------
drop table if exists x_tmp;
create table x_tmp
as 
select B.id,B.district_id,A.gap as gap_latest
--select B.*,A.*
from train_y B left join  train_y A on A.district_id=B.district_id 
and B.id= A.id + 144*7
;
--limit 10;


select count(*),sum(case when gap_latest is null then 1 else 0 end) from x_tmp;
-- 总纪录163491，其中有62554个为空,需要进行填充


--如果为空,则用同一时间同一地点平均值进行填充
drop table if exists train_x_gap_latest;
create table train_x_gap_latest
as
select A.id,A.district_id,
(case when A.gap_latest is null then B.gap_avg else A.gap_latest end) as gap_latest
from x_tmp A left join train_x_gap_average B on A.id=B.id and A.district_id=B.district_id
;

select count(*),sum(case when gap_latest is null then 1 else 0 end) from train_x_gap_latest;
--总纪录163491,其中6925个为空

drop table x_tmp;




