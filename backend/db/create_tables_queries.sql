-- drop table User;
-- drop table Category;
-- drop table Ticket;
-- drop table Transaction;
-- drop table Wish;
-- drop table Ticket_tag;
-- drop table Wish_tag;
-- drop table User_ticket;
-- drop table User_wish;

CREATE DATABASE IF NOT EXISTS ticket_arena;
USE ticket_arena;

CREATE TABLE IF NOT EXISTS User(
    user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(30),
    password VARCHAR(30),
    rank INT 
);

CREATE TABLE IF NOT EXISTS Category(
    category_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS Ticket(
    ticket_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(50),
    price INT,
    location VARCHAR(30),
    ticket_img VARCHAR(50),
    category_id INT REFERENCES Category(category_id),
    date Date NOT NULL 
);

CREATE TABLE IF NOT EXISTS Transaction(
    transaction_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    seller_id INT REFERENCES User(user_id),
    buyer_id INT REFERENCES User(user_id),
    status VARCHAR(20) 
);

CREATE TABLE IF NOT EXISTS Wish(
    wish_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id INT REFERENCES User(user_id),
    location VARCHAR(30),
    date Date 
);

CREATE TABLE IF NOT EXISTS Ticket_tag(
    ticket_id INT REFERENCES Ticket(ticket_id),
    word VARCHAR(20) 
);

CREATE TABLE IF NOT EXISTS Wish_tag(
    wish_id INT REFERENCES Wish(wish_id),
    word VARCHAR(20) 
);

CREATE TABLE IF NOT EXISTS User_ticket(
    user_id INT REFERENCES User(user_id),
    ticket_id INT REFERENCES Ticket(ticket_id)
);

CREATE TABLE IF NOT EXISTS User_wish(
    user_id INT REFERENCES User(user_id),
    wish_id INT REFERENCES Wish(wish_id)
);

-- SELECT *
-- FROM Ticket
-- ORDER BY date DESC;