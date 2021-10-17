CREATE TABLE address(
	address_id UUID NOT NULL,
	city VARCHAR(255) NOT NULL,
	street VARCHAR(255) NOT NULL,
	building INT NOT NULL,
	post_code VARCHAR(255) NOT NULL,

	PRIMARY KEY(address_id)
);

CREATE TABLE credit_card(
	credit_card_id UUID NOT NULL,
	provider VARCHAR(255) NOT NULL,
	number VARCHAR(255) NOT NULL,
	cvv INT NOT NULL,
	expire DATE NOT NULL,

	PRIMARY KEY(credit_card_id)
);

CREATE TABLE customer(
	customer_id UUID NOT NULL,
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
	password CHAR(106) NOT NULL,
	birth_date DATE NOT NULL,
	phone_number VARCHAR(255) NOT NULL,
	balance DECIMAL(10, 2) NOT NULL,
	address_id UUID NOT NULL,
	credit_card_id UUID NOT NULL,

	PRIMARY KEY(customer_id),
	CONSTRAINT fk_address
		FOREIGN KEY(address_id)
		REFERENCES address(address_id)
		ON DELETE RESTRICT,
	CONSTRAINT fk_credit_card
		FOREIGN KEY(credit_card_id)
		REFERENCES credit_card(credit_card_id)
		ON DELETE RESTRICT
);