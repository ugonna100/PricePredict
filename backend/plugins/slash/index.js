'use strict';

module.exports = function (fastify, opts, next) {
  fastify.get('/', (req, reply) =>  {
        reply.view('/pages/slash/index', {})
    });
    fastify.post('/:data', (req, reply) => {
        let payload = JSON.parse(req.params.data);
        const path = require('path');
        const priceAnalysis = require(path.resolve('lib/priceAnalysis.js'));
        priceAnalysis(payload)
          .then((data) => {
            payload.price = data.price;
            reply.send(payload.price);
          })
          .catch((err) => {
            if (err) throw err;
          })
        
    });

  next()
};