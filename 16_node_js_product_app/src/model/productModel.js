const mongoose = require("mongoose");

const ProductSchema = new mongoose.Schema({
  name: { type: String, required: true },
  price: { type: Number, required: true },
  description: String,
  createAt: { type: Date, default: Date.now },
});

module.exports = mongoose.model("Product", ProductSchema);
