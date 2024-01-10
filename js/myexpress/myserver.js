const express = require('express')
const app = express();
app.get('/api', (req, res) => {
    const data = {
        message: 'Hello World!'
    };
    res.json(data);
});

const port = process.env.PORT || 3000;
console.log(port);
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});