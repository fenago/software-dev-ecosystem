// server.js
const https = require('https');
const fs = require('fs');
const express = require('express');

const app = express();

// Load your SSL certificate and private key
const options = {
  key: fs.readFileSync('/certs/key.pem'),
  cert: fs.readFileSync('/certs/cert.pem')
};

// Simple GET route
app.get('/', (req, res) => {
  res.send('Hello, this is a secure SSL/TLS server!');
});

// Create HTTPS server
https.createServer(options, app).listen(443, () => {
  console.log('HTTPS Server listening on port 443');
});