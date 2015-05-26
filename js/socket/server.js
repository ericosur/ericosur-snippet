// http://www.gtwang.org/2014/03/socket-io-node-js-realtime-app.html
var http = require('http');
var url = require('url');
var fs = require('fs');
var io = require('socket.io') ();

var DEFAULT_PORT = 8001;

var server = http.createServer(function(req, resp) {
  console.log('connection');
  var path = url.parse(req.url).pathname;
  console.log('path: ' + path);

  switch (path) {
    case '/':
      resp.writeHead(200, {'Content-Type': 'text/html'});
      resp.write('it works!');
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

server.listen(DEFAULT_PORT);
var serv_io = io.listen(server);
serv_io.sockets.on('connection', function(socket) {
  socket.emit('message', {'message': 'hello world'});
  // send time to browser
  setInterval(function() {
    socket.emit('date', {'date': new Date()});
  }, 500);

  // recv from browser
  socket.on('client_data', function(data) {
    process.stdout.write(data.letter);
  });

  console.log('serv_io.sockets.on()');
});

