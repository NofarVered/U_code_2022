CREATE TABLE User(
    user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(30),
    passward VARCHAR(30),
    credit_card_id INT,
    rank INT 
);

CREATE TABLE Category(
    category_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20)
);

CREATE TABLE Ticket(
    ticket_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id INT REFERENCES User(user_id),
    title VARCHAR(50),
    price INT,
    location VARCHAR(30),
    ticket_img VARCHAR(50),
    category_id INT REFERENCES Category(category_id),
    date Date NOT NULL 
);

CREATE TABLE Transaction(
    transaction_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    seller_id INT REFERENCES User(user_id),
    buyer_id INT REFERENCES User(user_id),
    status VARCHAR(20) 
);

CREATE TABLE Wish(
    wish_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id INT REFERENCES User(user_id),
    location VARCHAR(30),
    date Date 
);

CREATE TABLE Ticket_tag(
    ticket_id INT REFERENCES Ticket(ticket_id),
    word VARCHAR(20) 
);

CREATE TABLE Wish_tag(
    wish_id INT REFERENCES Wish(wish_id),
    word VARCHAR(20) 
);

CREATE TABLE User_ticket(
    user_id INT REFERENCES User(user_id),
    ticket_id INT REFERENCES Ticket(ticket_id)
);

CREATE TABLE User_wish(
    user_id INT REFERENCES User(user_id),
    wish_id INT REFERENCES Wish(wish_id)
);