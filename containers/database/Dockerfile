FROM mariadb:10.5

ADD Server/utils/sql/database_full/quarm_2025-05-08-21_55.tar.gz /docker-entrypoint-initdb.d

ADD Server/loginserver/login_util/tblloginserversettings.sql /docker-entrypoint-initdb.d
RUN rm /docker-entrypoint-initdb.d/drop_system.sql

ADD containers/database/auto_create.sql /docker-entrypoint-initdb.d/z_auto_create.sql
ADD containers/database/launcher_boats.sql /docker-entrypoint-initdb.d/z_launcher_boats.sql
ADD containers/database/honzzquest_shit.sql /docker-entrypoint-initdb.d/z_honzzquest_shit.sql

ADD Server/loginserver/login_util/updates/2023_07_27_tblLoginServerAccounts.sql /docker-entrypoint-initdb.d/z_2023_07_27_tblLoginServerAccounts.sql
ADD Server/utils/sql/git/required/2024_12_23_player_events_tables.sql /docker-entrypoint-initdb.d/z_2024_12_23_player_events_tables.sql
ADD Server/utils/sql/git/required/2025_3_23_created_account_inventory_table.sql /docker-entrypoint-initdb.d/z_2025_3_23_created_account_inventory_table.sql
ADD Server/utils/sql/git/required/2025_06_14_guild_raid_enabled.sql /docker-entrypoint-initdb.d/z_2025_06_14_guild_raid_enabled.sql
