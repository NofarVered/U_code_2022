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

CREATE TABLE IF NOT EXISTS Event(
    event_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(50),
    location VARCHAR(30),
    event_img VARCHAR(50),
    category_id INT REFERENCES Category(category_id),
    date Date NOT NULL 
);

CREATE TABLE IF NOT EXISTS Ticket(
    ticket_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id INT REFERENCES User(user_id),
    price INT,
    ticket_img VARCHAR(50),
    event_id INT REFERENCES Event(event_id),
    seat VARCHAR(30)
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

CREATE TABLE IF NOT EXISTS Event_tag(
    event_id INT REFERENCES Event(event_id),
    word VARCHAR(20) 
);

CREATE TABLE IF NOT EXISTS Wish_tag(
    wish_id INT REFERENCES Wish(wish_id),
    word VARCHAR(20) 
);

CREATE TABLE IF NOT EXISTS User_wish(
    user_id INT REFERENCES User(user_id),
    wish_id INT REFERENCES Wish(wish_id)
);


CREATE OR REPLACE VIEW Temp_event as
SELECT DISTINCT e.event_id
FROM Event AS e, Event_tag AS et
WHERE (e.event_id = et.event_id) AND (et.word IN ("Bon", "coldplay")); 

-- SELECT *
-- FROM Event, (SELECT DISTINCT e.event_id
-- FROM Event AS e, Event_tag AS et
-- WHERE (e.event_id = et.event_id) AND (et.word IN ("Bon", "coldplay"))) As Temp_event
-- WHERE Event.event_id = Temp_event.event_id;
