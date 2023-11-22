const { pool } = require("../models/todoModel");

const todoAdd = async (req, res) => {
  try {
    const { name, description, completed } = req.body;

    const insertQuery = `
            INSERT INTO todo(name,description, completed, created_at, updated_at) VALUES ($1, $2, $3, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP) RETURNING*;
        `;

    const insertValues = [name, description, completed];

    const client = await pool.connect();
    const insertResault = await client.query(insertQuery, insertValues);
    const todoAdded = insertResault.rows[0];
    client.release();
    return res.status(201).json(todoAdded);
  } catch (error) {
    console.log("Kayıt oluşturlmadı..", error);
    return res.status(500).json({
      success: false,
      message: "Kayıt oluşturulmadı..",
    });
  }
};

const totoGetAll = async (req, res) => {
  try {
    const query = "SELECT * FROM todo";

    const client = await pool.connect();
    const resault = await client.query(query);
    const todos = resault.rows;
    client.release();

    return res.status(200).json(todos);
  } catch (error) {
    return res.status(500).json({
      success: false,
      message: "Kayıtlar alınamadı",
    });
  }
};

const todoDelete = async (req, res) => {
  try {
    const id = req.params.id;

    const deleteQuery = `DELETE FROM todo WHERE id = $1 RETURNING*;`;

    const values = [id];

    const client = await pool.connect();
    const resault = await client.query(deleteQuery, values);
    client.release();

    const deleteTodo = resault.rows[0];

    if (!deleteTodo) {
      return res.status(404).json({
        success: false,
        message: "Kayıt bulunamadı",
      });
    }

    return res.status(200).json(deleteTodo);
  } catch (error) {
    console.error("Kayıt silinirken hata oluştu..", error);
    return res.status(500).json({
      success: false,
      message: "Kayıt silinirken hata oluştu..",
    });
  }
};

const todoGet = async (req, res) => {
  try {
    const id = req.params.id;

    const getQuery = `SELECT * FROM todo WHERE id = $1`;

    const values = [id];

    const client = await pool.connect();
    const resault = await client.query(getQuery, values);
    client.release();

    const todo = resault.rows[0];

    if (!todo) {
      return res.status(404).json({
        success: false,
        message: "kayıt bulunamadı",
      });
    }

    return res.status(200).json(todo);
  } catch (error) {
    console.error("Kayıt alınırken hata oluştu..", error);
    return res.status(500).json({
      success: false,
      message: "Kayıt alınırken hata oluştu..",
    });
  }
};

const todoUpdate = async (req, res) => {
  try {
    const id = req.params.id;
    const { name, description, completed } = req.body;

    const updateQuery = `
      UPDATE todo
      SET name = $1, description = $2, completed = $3, updated_at = CURRENT_TIMESTAMP
      WHERE id = $4
      RETURNING *;
    `;

    const values = [name, description, completed, id];

    const client = await pool.connect();
    const result = await client.query(updateQuery, values);
    client.release();

    const updatedTodo = result.rows[0];
    console.log(updatedTodo);

    if (!updatedTodo) {
      return res.status(404).json({
        success: false,
        message: "kayıt bulunamadı",
      });
    }

    return res.status(200).json(updatedTodo);
  } catch (error) {
    console.error("Kayıt güncellenirken hata oluştu..", error);
    return res.status(500).json({
      success: false,
      message: "Kayıt güncellenirken hata oluştu..",
    });
  }
};

module.exports = { todoAdd, totoGetAll, todoDelete, todoGet, todoUpdate };
