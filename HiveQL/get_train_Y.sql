create table train_Y as select (day(o_date)-1)*144+time_slice as id,o_date,time_slice,start_district_id as district_id,sum(gap) as gap from train_order group by o_date,time_slice,start_district_id order by o_date,time_slice,start_district_id;
