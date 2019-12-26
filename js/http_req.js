// file: http_req.js
// example to use http(s) request for random numbers
//
// example from:
// https://docs.nodejitsu.com/articles/HTTP/clients/how-to-create-a-HTTP-request/
//

// www.random.org now use https
//The url we want is: 'www.random.org/integers/?num=1&min=1&max=10&col=1&base=10
//&format=plain&rnd=new'

(function() {

  var mymin = '1';
  var mymax = '199';

  var options = {
    host: 'www.random.org',
    path: '/integers/?num=17&min=' + mymin + '&max=' + mymax
      + '&col=1&base=10&format=plain&rnd=new'
  };

  callback = function(response) {
    var str = '';

    //another chunk of data has been recieved, so append it to `str`
    response.on('data', function (chunk) {
      str += chunk;
    });

    //the whole response has been recieved, so we just print it out here
    response.on('end', function () {
      console.log(str);
    });
  }

  console.log('request random.org for random numbers...');
  console.log('options.host: ' + options['host']);
  var http = require('https');
  http.request(options, callback).end();

})();
