// http://www.gtwang.org/2014/03/socket-io-node-js-realtime-app.html
var http = require('http');
var url = require('url');
var fs = require('fs');
var io = require('socket.io');

var server = http.createServer(function(req, resp) {
  console.log('connection');
  var path = url.parse(req.url).pathname;
  console.log('path: ' + path);

  switch (path) {
    case '/':
      resp.writeHead(200, {'Content-Type': 'text/html'});
      resp.write('hello, world!');
      resp.end();
      break;
    case '/socket.html':
      fs.readFile(__dirname + path, function(err, data) {
        if (err) {
          resp.writeHead(404);
          resp.write('opps! this does not exist - 404');
        } else {
          resp.writeHead(200, {'Content-Type': 'text/html'});
          resp.write(data, "utf8");
        }
        resp.end();
      });
      break;
    default:
      resp.writeHead(404);
      resp.write('default not exist');
      resp.end();
      break;
  }
});

server.listen(8001);
io.listen(server);

