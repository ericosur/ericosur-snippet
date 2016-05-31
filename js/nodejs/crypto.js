/// https://nodejs.org/dist/latest-v6.x/docs/api/crypto.html

var crypto;
try {
    crypto = require('crypto');
} catch (err) {
    console.log('crypto support is disabled!');
    return;
}

const secret = 'abcdefg';
const hash = crypto.createHmac('sha256', secret)
                    .update('I love cupcakes')
                    .digest('hex');
console.log(hash);
