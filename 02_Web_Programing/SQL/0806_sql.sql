CREATE TABLE my_table (
	my_field1 INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	my_field2 VARCHAR(50),
	my_field3 DATE NOT NULL DEFAULT current_timestamp
);

ALTER TABLE my_table ADD my_field4 int NOT NULL;

DROP TABLE my_table;