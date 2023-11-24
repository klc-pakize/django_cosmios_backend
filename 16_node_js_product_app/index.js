const express = require("express");
const mongoose = require("mongoose");
const bodyParser = require("body-parser");

const productRouter = require("./src/router/productRouter");

const app = express();

app.use(bodyParser.json());
app.use(productRouter);

const username = "admin";
const password = "nag3V9bHxv77JsnG";
const databasename = "products";

mongoose
  .connect(
    `mongodb+srv://${username}:${password}@cluster0.akjny1l.mongodb.net/${databasename}?retryWrites=true&w=majority`
  )
  .then(() => {
    console.log("Connected to database");
  })
  .catch((error) => {
    console.log(error);
  });

app.listen(5000, () => {
  console.log("Server 5000 portun çalışyor.");
});
