create table test_targets as select A.id, A.o_date, A.time_slice,B.district_id from targets A join cluster_map B order by A.id,B.district_id;
