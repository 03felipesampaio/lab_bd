SELECT COUNT(*) FROM results WHERE "position"=1 AND driverid=1;
SELECT MIN(RA."year"), MAX(RA."year") FROM results JOIN races RA USING (raceid)	WHERE driverid=1;