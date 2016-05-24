-------------------------------test_x_dayofweek----------------------------
--每周第几天
create table test_x_dayofweek as
select 
id,district_id,
--*,
PMOD(DATEDIFF(o_date, '2012-01-01'), 7)+1 as dayofweek
from test_t
-- where o_date='2016-01-24'
-- limit 10
;

select count(*) from test_x_dayofweek;



-------------------------------test_x_ifweekday----------------------------
--是否为工作日 id,district_id,
create table test_x_ifweekday as
select id,district_id,
(case 
when PMOD(DATEDIFF(o_date, '2012-01-01'), 7)+1 <=5 THEN 1
else 0
end )
as if_weekday
from test_t 
;
select count(*) from test_x_ifweekday;




-------------------------------test_x_dayofweekday----------------------------
--一周的第几个工作日 id,district_id,
create table test_x_dayofweekday as
--select *,
select id,district_id,
(case 
when PMOD(DATEDIFF(o_date, '2012-01-01'), 7)+1 <=5 THEN PMOD(DATEDIFF(o_date, '2012-01-01'), 7)+1
else 0
end )
as dayofweekday
from test_t 
--;

-- where o_date='2016-01-28'
-- limit 10
;
select count(*) from test_x_dayofweekday;



-------------------------------test_x_iffestival----------------------------
--是否为节日id,district_id,#select *,
create table test_x_iffestival as
select id,district_id,
(case 
when o_date >= '2016-01-01' and o_date <= '2016-01-03' THEN 1
else 0
end )
as if_festival
from test_t
; 
--where o_date='2016-01-05'
--limit 10
--;

select count(*) from test_x_iffestival;


-------------------------------test_x_ifmpeak----------------------------
--是否为早高峰，工作日且时间为7到9点，也就是time_slice在42~54之间
create table test_x_ifmpeak as
--select *,
select id,district_id,
(case 
when PMOD(DATEDIFF(o_date, '2012-01-01'), 7)+1 <=5 and time_slice>=42 and time_slice<=54 
THEN 1
else 0
end )
as if_mpeak
from test_t 
;
-- where o_date='2016-01-04' and time_slice<54 and time_slice>40
-- limit 100
-- ;
select count(*) from test_x_ifmpeak;

-------------------------------test_x_ifepeak----------------------------
--是否为晚高峰，工作日且时间晚上为17到19点，也就是time_slice在102～114之间
create table test_x_ifepeak as
--select *,
select id,district_id,
(case 
when PMOD(DATEDIFF(o_date, '2012-01-01'), 7)+1 <=5 and time_slice>=102 and time_slice<=114 
THEN 1
else 0
end )
as if_epeak
from test_t 
;
-- where o_date='2016-01-04' and time_slice<54 and time_slice>40
-- limit 100
-- ;
select count(*) from test_x_ifepeak;




















