-- allow vah shir
UPDATE char_create_combinations SET expansions_req = 0 WHERE race = 130 AND class <= 15;

-- open up all zones to non-GMs
UPDATE zone SET min_status = 0;