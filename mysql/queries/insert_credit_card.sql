INSERT INTO credit_card(
	credit_card_id, provider, number, cvv, expire
) VALUES(
	UUID_TO_BIN(%s), %s, %s, %s, %s
);