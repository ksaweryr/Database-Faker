INSERT INTO credit_card(
	credit_card_id, provider, number, cvv, expire
) VALUES(
	%s, %s, %s, %s, %s
);