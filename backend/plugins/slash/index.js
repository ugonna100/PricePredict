'use strict';

module.exports = function (fastify, opts, next) {
  fastify.get('/', (req, reply) => {
        reply.view('/pages/slash/index', {})
    });
    fastify.post('/:data', (req, reply) => {
        let payload = JSON.parse(req.params.data);

        reply.send(payload.itemName + 'helloworld');
    });

  next()
};