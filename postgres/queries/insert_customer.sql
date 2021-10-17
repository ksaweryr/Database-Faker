INSERT INTO customer(
	customer_id, first_name, last_name, password, birth_date, phone_number,
	balance, address_id, credit_card_id
) VALUES(
	%s, %s, %s, %s, %s, %s, %s, %s, %s
);