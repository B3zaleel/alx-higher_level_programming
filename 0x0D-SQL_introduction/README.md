# SQL - Introduction

This project contains some tasks for learning the basics about **SQL** using the **MySQL** DBMS.

## Tasks To Complete

+ [x] 0\. List databases <br/>_**[0-list_databases.sql](0-list_databases.sql)**_ contains a script that lists all databases of the MySQL server.
+ [x] 1\. Create a database <br/>_**[1-create_database_if_missing.sql](1-create_database_if_missing.sql)**_ contains a script that creates the database ``hbtn_0c_0`` in the MySQL server if it doesn't exist.
+ [x] 2\. Delete a database <br/>_**[2-remove_database.sql](2-remove_database.sql)**_ contains a script that deletes the database `hbtn_0c_0` in the MySQL server if it doesn't exist.
+ [x] 3\. List tables <br/>_**[3-list_tables.sql](3-list_tables.sql)**_ contains a script that lists all the tables of a database in the MySQL server.
+ [x] 4\. First table <br/>_**[4-first_table.sql](4-first_table.sql)**_ contains a script that creates a table called first_table in the current database in your MySQL server.
  + The description of `first_table`:
  ```python
  class first_table:
      id: INT
      name: VARCHAR(256)
  ```
+ [x] 5\. Full description <br/>_**[5-full_table.sql](5-full_table.sql)**_ contains a script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in the MySQL server.
+ [x] 6\. List all in table <br/>_**[6-list_values.sql](6-list_values.sql)**_ contains a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in the MySQL server.
+ [x] 7\. First add <br/>_**[7-insert_value.sql](7-insert_value.sql)**_ contains a script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in the MySQL server.
  + The row:
  ```json
  {"id": 89, "name": "Best School"}
  ```
+ [x] 8\. Count 89 <br/>_**[8-count_89.sql](8-count_89.sql)**_ contains a script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in the MySQL server.
+ [x] 9\. Full creation <br/>_**[9-full_creation.sql](9-full_creation.sql)**_ contains a script that creates a table `second_table` if it doesn't exist in the database `hbtn_0c_0` in the MySQL server, and adds multiples rows.
  + The description of `second_table`:
  ```python
  class second_table:
      id: INT
      name: VARCHAR(256)
      score: INT
  ```
  + The script should create these records:
  ```json
  [
    {"id": 1, "name": "John", "score": 10},
    {"id": 2, "name": "Alex", "score": 3},
    {"id": 3, "name": "Bob", "score": 14},
    {"id": 4, "name": "George", "score": 8}
  ]
  ```
+ [x] 10\. List by best <br/>_**[10-top_score.sql](10-top_score.sql)**_ contains a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in the MySQL server. The records should be ordered by `score` (top first) and the results should display the `score` first then the `name`.
+ [x] 11\. Select the best <br/>_**[11-best_score.sql](11-best_score.sql)**_ contains a script that ists all records with a `score >= 10` in the table `second_table` of the database `hbtn_0c_0` in the MySQL server. The records should be ordered by `score` (top first) and the results should display the `score` first then the `name`.
+ [x] 12\. Cheating is bad <br/>_**[12-no_cheating.sql](12-no_cheating.sql)**_ contains a script that updates the score of _Bob_ to _10_ in the table `second_table`.
+ [x] 13\. Score too low <br/>_**[13-change_class.sql](13-change_class.sql)**_ contains a script that removes all records with a `score <= 5` in the table `second_table` of the database `hbtn_0c_0` in the MySQL server.
+ [x] 14\. Average <br/>_**[14-average.sql](14-average.sql)**_ contains a script that computes the `score` average of all records in the table `second_table` of the database `hbtn_0c_0` in the MySQL server. The result column name should be `average`.
+ [x] 15\. Number by score <br/>_**[15-groups.sql](15-groups.sql)**_ contains a script that lists the number of records with the same `score` in the table `second_table` of the database `hbtn_0c_0` in the MySQL server. The list should be sorted by the number of records (descending). The result should display the `score` first then the number of records for this `score` with the label `number`.
+ [x] 16\. Say my name <br/>_**[16-square.sql](16-square.sql)**_ contains a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in the MySQL server. The results should display the `score` and the `name` (in this order) and they should be listed by descending `score` but rows without a `name` value shouldn't be included.
+ [x] 17\. Go to UTF8 <br/>_**[100-move_to_utf8.sql](100-move_to_utf8.sql)**_ contains a script that converts the following to UTF8 (`utf8mb4`, collate `utf8mb4_unicode_ci`) in the MySQL server:
  + Database `hbtn_0c_0`
  + Table `first_table` in database `hbtn_0c_0`
  + Field `name` in `first_table`
+ [x] 18\. Temperatures #0 <br/>_**[101-avg_temperatures.sql](101-avg_temperatures.sql)**_ contains a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending). The table in [temperatures.sql](temperatures.sql) is used for this task.
+ [x] 19\. Temperatures #1 <br/>_**[102-top_city.sql](102-top_city.sql)**_ contains a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending). The table in [temperatures.sql](temperatures.sql) is used for this task.
+ [x] 20\. Temperatures #2 <br/>_**[103-max_state.sql](103-max_state.sql)**_ contains a script that displays the max temperature of each state (ordered by State name). The table in [temperatures.sql](temperatures.sql) is used for this task.
