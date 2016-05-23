create table train_x_gap1 as select A.id,A.district_id,B.gap as gap1 from train_y A left join train_y B on A.district_id=B.district_id where (A.id - B.id)=1;
