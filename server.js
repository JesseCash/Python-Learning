const express = require("express");
const mysql = require("mysql");
const cors = require("cors");
const bcrypt = require("bcrypt");

const app = express();
app.use(express.json());
app.use(cors());

// MySQL Database Connection
const db = mysql.createConnection({
    host: "localhost",
    user: "root",  // Your MySQL username
    password: "",  // Your MySQL password
    database: "your_database_name"
});

db.connect(err => {
    if (err) throw err;
    console.log("MySQL Connected...");
});

// Login Endpoint
app.post("/login", (req, res) => {
    const { username, password } = req.body;
    const sql = "SELECT * FROM Users WHERE Email = ?"; // Assuming email is used for login

    db.query(sql, [username], (err, results) => {
        if (err) return res.json({ success: false, message: "Database error" });

        if (results.length > 0) {
            const user = results[0];
            bcrypt.compare(password, user.PasswordHash, (err, match) => {
                if (match) {
                    res.json({ success: true, message: "Login successful" });
                } else {
                    res.json({ success: false, message: "Incorrect password" });
                }
            });
        } else {
            res.json({ success: false, message: "User not found" });
        }
    });
});

// Start Server
app.listen(3000, () => {
    console.log("Server running on port 3000");
});
