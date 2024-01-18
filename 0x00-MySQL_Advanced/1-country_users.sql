-- Create a table with unique email addresses
CREATE TABLE
    IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(255) UNIQUE NOT NULL,
        name VARCHAR(255),
        country ENUM ('US', 'CA', 'MX') NOT NULL DEFAULT 'US'
    );