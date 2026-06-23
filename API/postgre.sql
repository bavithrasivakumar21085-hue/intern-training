CREATE TABLE users(
user_id SERIAL PRIMARY KEY,
user_name VARCHAR(100) NOT NULL,
user_email VARCHAR(150) UNIQUE
);

INSERT INTO users (user_name,user_email)
values('Bavithra', 'bavithra123@gmail.com');

Insert into users (user_name,user_email)
Values
('Kiruthiga', 'kiruthiga123@gmail.com'),
('Prakash', 'prakash123@gmail.com'),
('Velayutham', 'velayutham123@gmail.com'),
('Iniyan','iniyan123@gmail.com'),
('Vishrava','vishrava123@gmail.com');


SELECT * FROM users
ORDER BY user_name;

SELECT * FROM users
WHERE user_name ILIKE 'v%'