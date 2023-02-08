-- Creating users table
CREATE TABLE users (
	id int NOT NULL,
	name VARCHAR ( 255 ) NOT NULL,
	street VARCHAR ( 255) NOT NULL,
	city VARCHAR ( 255 ) NOT NULL,
	zip VARCHAR ( 255 ) NOT NULL
	);

-- Checking users table
SELECT * FROM users;

-- Drop users table
DROP TABLE public.users CASCADE;