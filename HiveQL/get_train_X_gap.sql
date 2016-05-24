-------------------------train_x_gap1----------------------------------------------------
drop table if exists train_x_gap1;
create table train_x_gap1 
	as select A.id,A.district_id,B.gap as gap1 
	from train_y A left join train_y B on A.district_id=B.district_id and A.id = B.id+1;

--select count(*) from train_x_gap1;

--train_x_gap1: 152653, train_y:163491



-------------------------train_x_gap2----------------------------------------------------
drop table if exists train_x_gap2;
create table train_x_gap2
	as select A.id,A.district_id,B.gap as gap2 
	from train_y A left join train_y B on A.district_id=B.district_id and A.id = B.id + 2;

--select count(*) from train_x_gap2;

--train_x_gap2: 151909, train_y:163491



-------------------------train_x_gap3----------------------------------------------------
drop table if exists train_x_gap3;
create table train_x_gap3
	as select A.id,A.district_id,B.gap as gap3
	from train_y A left join train_y B on A.district_id=B.district_id and A.id = B.id + 3;

--select count(*) from train_x_gap3;

--train_x_gap3: 151410, train_y:163491
