INSERT INTO address(
	address_id, city, street, building, post_code
) VALUES(
	UUID_TO_BIN(%s), %s, %s, %s, %s
);