CREATE TABLE IF NOT EXISTS usuarios (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL
);

INSERT INTO usuarios (nombre, email)
VALUES
  ('Juan', 'juan@test.com'),
  ('Maria', 'maria@test.com')
ON CONFLICT (email) DO NOTHING;