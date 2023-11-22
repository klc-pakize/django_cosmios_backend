const { Pool } = require("pg");

const pool = new Pool({
  user: "postgres",
  host: "localhost",
  database: "todoapp",
  password: "Sadi1430",
  port: 5432,
});

const createTodoTable = async () => {
  try {
    const createTableQuery = `
            CREATE TABLE todo(
                id SERIAL PROMARY KEY,
                name VARCHAR NOT NULL,
                description TEXT NOT NULL,
                completed BOOLEAN DEFAULT FALSE,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            )
            `;

    const client = await pool.connect();
    await client.query(createTableQuery);
    client.release();

    console.log("Tablo başarılı bir şekilde oluşturuldu.");
  } catch (error) {
    console.log("Tablo oluşturulmadı", error);
  }
};

module.exports = { pool, createTodoTable };
