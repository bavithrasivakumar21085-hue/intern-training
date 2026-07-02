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

alter table users
add country Varchar(20);

update users
set country='India'
where user_id=1;

update users
set country='India'
where user_id=4;

update users
set country='India'
where user_id=6;

update users
set country='us'
where user_id=5;

update users
set country='us'
where user_id=2;

update users
set country='uk'
where user_id=3;

SELECT * FROM users
ORDER BY user_name;

SELECT * FROM users
WHERE user_name ILIKE 'v%'

create table posts(
post_id serial primary key,
post_name varchar(255) not null,
user_id int,
constraint fk_user foreign key(user_id)
references users(user_id)
);

select * from posts;

insert into posts(post_name)
values('git');
update posts set user_id=1 where post_id =1;

insert into posts(post_name,user_id)
values('python',2);

insert into posts(post_name,user_id)
values
('postgres',3),
('python advanced',2),
('sql',4),
('oops',5),
('postgres advanced',6);

select users.user_id, users.user_name, posts.post_name
from users
Inner Join posts ON users.user_id=posts.user_id;


select u.user_id, u.user_name, p.post_name
from users u
left join posts p 
ON u.user_id=p.user_id;


select count(user_id), country
from users
group by country;
