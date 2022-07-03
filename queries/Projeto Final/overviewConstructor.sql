SELECT COUNT(*) FROM results WHERE position=1 AND constructorid=1;
SELECT COUNT(DISTINCT(driverid)) FROM results WHERE constructorid=1;
SELECT MIN(RA.year), MAX(RA.year) FROM results JOIN races RA USING (raceid)	WHERE constructorid=1;