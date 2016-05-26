insert overwrite local directory 'DD-competition/data/test_t' 
	select concat(district_id,',',o_date,'-',time_slice) from test_t;
--insert overwrite local directory 'DD-competition/data/train_y' select gap from train_y;
--insert overwrite local directory 'DD-competition/data/test_x_ifepeak' select if_epeak from test_x_ifepeak;

--insert overwrite local directory 'DD-competition/data/test_x_iffestival' select if_festival from test_x_iffestival;

--insert overwrite local directory 'DD-competition/data/test_x_ifmpeak' select if_mpeak from test_x_ifmpeak;

--insert overwrite local directory 'DD-competition/data/test_x_ifweekday' select if_weekday from test_x_ifweekday;

insert overwrite local directory 'DD-competition/data/train_x_gap1' select gap1 from train_x_gap1;
insert overwrite local directory 'DD-competition/data/train_x_gap2' select gap2 from train_x_gap2;
insert overwrite local directory 'DD-competition/data/train_x_gap3' select gap3 from train_x_gap3;

insert overwrite local directory 'DD-competition/data/test_x_gap1' select gap1 from test_x_gap1;
insert overwrite local directory 'DD-competition/data/test_x_gap2' select gap2 from test_x_gap2;
insert overwrite local directory 'DD-competition/data/test_x_gap3' select gap3 from test_x_gap3;




insert overwrite local directory 'DD-competition/data/train_x_dayofweek' select dayofweek from train_x_dayofweek;
insert overwrite local directory 'DD-competition/data/train_x_dayofweekday' select dayofweekday from train_x_dayofweekday;

insert overwrite local directory 'DD-competition/data/test_x_dayofweek' select dayofweek from test_x_dayofweek;
insert overwrite local directory 'DD-competition/data/test_x_dayofweekday' select dayofweekday from test_x_dayofweekday;	



insert overwrite local directory 'DD-competition/data/train_x_gap_latest' select gap_laterst from train_x_gap_latest;
insert overwrite local directory 'DD-competition/data/test_x_gap_latest' select gap_latest from test_x_gap_latest;


insert overwrite local directory 'DD-competition/data/train_x_gap_avg' select gap_avg from train_x_gap_avg;
insert overwrite local directory 'DD-competition/data/test_x_gap_avg' select gap_avg from test_x_gap_avg;







