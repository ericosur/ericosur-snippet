// file: http_req.js
// example to use http(s) request for random numbers
//
// example from:
// https://docs.nodejitsu.com/articles/HTTP/clients/how-to-create-a-HTTP-request/
//

// www.random.org now use https
//The url we want is:
// https://www.random.org/gaussian-distributions/?num=10&mean=100&stdev=15&dec=6
// &col=1&notation=scientific&format=plain&rnd=new

(function() {

  var mean = '100';
  var stdev = '15';

  var options = {
    host: 'www.random.org',
    path: '/gaussian-distributions/?num=25&mean=' + mean + '&stdev=' + stdev
      + '&dec=6&col=1&notation=scientific&format=plain&rnd=new'
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

  console.log('request random.org for gaussian-distributions numbers...');
  var http = require('https');
  http.request(options, callback).end();

})();
