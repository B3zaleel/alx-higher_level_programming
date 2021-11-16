-- Changes a property of a database in the server
ALTER DATABASE hbtn_0c_0
    DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Changes the database in use for the next set of instructions.
USE hbtn_0c_0;
-- Changes the properties of a table in the database
ALTER TABLE first_table
    DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Changes the properties of a column in a table in the database
ALTER TABLE first_table
    MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL;
