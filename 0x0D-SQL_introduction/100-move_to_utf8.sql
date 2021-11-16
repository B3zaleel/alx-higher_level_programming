-- Changes a property of a database in the server
ALTER DATABASE hbtn_0c_0
    DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Changes the properties of a table in the database
ALTER TABLE first_table
    CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Changes the properties of a column in a table in the database
ALTER TABLE first_table MODIFY
    name VARCHAR(256)
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
