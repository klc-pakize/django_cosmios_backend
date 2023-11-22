const router = require("express").Router();
const todoController = require("../controllers/todoControllers");

// const express = require("express");
// const router = express.Router();

router.post("/todo", todoController.todoAdd);
router.get("/todo", todoController.totoGetAll);
router.delete("/todo/:id", todoController.todoDelete);
router.get("/todo/:id", todoController.todoGet);
router.put("/todo/:id", todoController.todoUpdate);

module.exports = router;
