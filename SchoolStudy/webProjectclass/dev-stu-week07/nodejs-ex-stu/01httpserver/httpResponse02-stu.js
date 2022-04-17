// ./01httpserver/httpResponse.js
var http = require('http');
var server = http.createServer(function(req, res) {
	res.statusCode = 200;
	res.statusMessage = 'OKOK';
	res.setHeader('content-type', 'text/html');

	res.write('<html><body><h1>Hello World</h1></body></html>');
	res.end();  // 응답 메시지 완료
})
  .listen(3000, () => { // 서버 연결
  	console.log('server on : 3000 port')
});