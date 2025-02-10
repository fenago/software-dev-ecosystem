// server.js
const express = require("express");
const jwt = require("jsonwebtoken");
const app = express();

const rolesConfig = require("./rolesConfig");

app.use(express.json());

// A mock login route that issues tokens
app.post("/login", (req, res) => {
  // In a real app, you'd validate username/password from DB.
  // We'll just accept a role from the request body.
  const { role } = req.body;

  // If the role isn't recognized, deny.
  if (!rolesConfig[role]) {
    return res.status(400).json({ message: "Invalid role." });
  }

  // Sign a simple JWT with the role in payload
  const token = jwt.sign({ role }, "SECRET_KEY", { expiresIn: "1h" });
  return res.json({ token });
});

// Middleware to require a given permission
function requirePermission(permission) {
  return function (req, res, next) {
    try {
      // Extract token from headers
      const authHeader = req.headers.authorization;
      if (!authHeader) {
        return res.status(401).json({ message: "No authorization header." });
      }
      const token = authHeader.split(" ")[1];
      const decodedToken = jwt.verify(token, "SECRET_KEY");
      const userRole = decodedToken.role;

      // Check if user role has required permission
      if (!rolesConfig[userRole] || !rolesConfig[userRole].includes(permission)) {
        return res.status(403).json({ message: "Access Denied." });
      }

      // Attach user data to request if needed
      req.user = decodedToken;
      next();
    } catch (error) {
      return res.status(401).json({ message: "Unauthorized." });
    }
  };
}

// Protected routes
app.post("/create", requirePermission("create"), (req, res) => {
  res.status(201).json({ message: "Item created." });
});

app.get("/read", requirePermission("read"), (req, res) => {
  res.status(200).json({ items: ["Item1", "Item2"] });
});

app.put("/update", requirePermission("update"), (req, res) => {
  res.status(200).json({ message: "Item updated." });
});

app.delete("/delete", requirePermission("delete"), (req, res) => {
  res.status(200).json({ message: "Item deleted." });
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});