-- A SQL script that creates a function SafeDiv that divides (and returns).
DELIMITER //
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT
BEGIN
	DECLARE answer FLOAT;
	IF b = 0 THEN
		SET answer = 0;
	ELSE
		SET answer = a / b;
	END IF;
	RETURN answer;
END;
//
