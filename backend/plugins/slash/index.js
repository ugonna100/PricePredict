'use strict';

module.exports = function (fastify, opts, next) {
  fastify.get('/', (req, reply) =>  {
        reply.view('/pages/slash/index', {})
    });
    fastify.get('/predict', (req, reply) =>  {
      reply.view('/pages/predict/index', {})
  });
    fastify.post('/predict:data', (req, reply) => {
        let payload = JSON.parse(req.params.data);
        let desc = payload.description;
        const path = require('path');
        const priceAnalysis = require(path.resolve('lib/priceAnalysis.js'));
        priceAnalysis(desc)
          .then((data) => {
            payload.price = data.price;
            reply.send(payload.price);
          })
          .catch((err) => {
            if (err) throw err;
          })
        
    });

  next();
};