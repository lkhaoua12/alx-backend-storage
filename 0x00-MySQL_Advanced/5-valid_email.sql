--  a SQL script that creates a trigger that resets the attribute valid_email
CREATE TRIGGER check_valid_email
AFTER
UPDATE
    ON users FOR EACH ROW IF new.email != old.email THEN
SET
    valid_email = 0;

END IF;