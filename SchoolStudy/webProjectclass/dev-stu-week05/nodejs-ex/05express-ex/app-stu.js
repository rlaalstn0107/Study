// main.js: express 서버
var express = require('express');
var app = express();

var user_stu = require('./routes/user-stu');

app.get('/', function(req, res) {
    res.send('<h1><u>Hello World!!!!!!!!!!!!!!!!!!!!</u></h1>');
});

app.use('/user', user_stu);   // /user 일때 ./routes/user-stu 로 가게끔 만든다




// app.get('/user/:id', function(req, res) {
//     res.send('Received a GET request, param:' + req.params.id);
// });

// app.post('/user', function(req, res) {
//     res.json({ success: true })
// });

// app.put('/user', function(req, res) {
//     res.status(400).json({ message: 'Hey, you. Bad Request!' });
// });

// app.delete('/user', function(req, res) {
//     res.send('Received a DELETE request');
// });

app.listen(3000, function() {
    console.log('Example App listening on port 3000');
});