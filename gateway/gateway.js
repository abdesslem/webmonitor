var http = require('http');
var url = require('url');
var jwt = require('jsonwebtoken');
var mongoose = require('mongoose');
var morgan = require('morgan');
var sprintf = require('sprintf');
var Q = require('q');
var _ = require('underscore');

var logger = require('./logger');


var httpLogger = morgan('combined', { stream: logger.stream });

function toBase64(obj) {
    return new Buffer(JSON.stringify(obj)).toString('base64');
}


var secretKey = "super secret jwt key";
var issuerStr = "Sample API Gateway"

function send401(res) {
    res.statusCode = 401;
    res.end();
}

function send500(res) {
    res.statusCode = 500;
    res.end();
}


/*
 * Simple login: returns a JWT if login data is valid.
 */
function login(req, res) {
}

/*
 * Authentication validation using JWT. Strategy: find existing user.
 */
function validateAuth(data, callback) {
}

function roleCheck(user, service) {
    var intersection = _.intersection(user.roles, service.authorizedRoles);
    return intersection.length === service.authorizedRoles.length;
}

/*
 * Parses the request and dispatches multiple concurrent requests to each
 * internal endpoint. Results are aggregated and returned.
 */
function serviceDispatch(req, res) {
    var parsedUrl = url.parse(req.url);

    Service.findOne({ url: parsedUrl.pathname }, function(err, service) {
        if(err) {
            logger.error(err);
            send500(res);
            return;
        }

        var authorized = roleCheck(req.context.authPayload.user, service);
        if(!authorized) {
            send401(res);
            return;
        }

        // Fanout all requests to all related endpoints.
        // Results are aggregated (more complex strategies are possible).
        var promises = [];
        service.endpoints.forEach(function(endpoint) {
            logger.debug(sprintf('Dispatching request from public endpoint ' +
                '%s to internal endpoint %s (%s)',
                req.url, endpoint.url, endpoint.type));

                promises.push(httpPromise(req, endpoint.url,
                    endpoint.type === 'http'));
            }
        });

        //Aggregation strategy for multiple endpoints.
        Q.allSettled(promises).then(function(results) {
            var responseData = {};

            results.forEach(function(result) {
                if(result.state === 'fulfilled') {
                    responseData = _.extend(responseData, result.value);
                } else {
                    logger.error(result.reason.message);
                }
            });

            res.setHeader('Content-Type', 'application/json');
            res.end(JSON.stringify(responseData));
        });
    }, 'services');
}

var server = http.createServer(function(req, res) {
    httpLogger(req, res, function(){});

    // Login endpoint
    if(req.url === "/login" && req.method === 'POST') {
        doLogin(req, res);
        return;
    }

    // Authentication
    var authHeader = req.headers["authorization"];
    validateAuth(authHeader, function(authPayload) {
        if(!authPayload) {
            send401(res);
            return;
        }

        // We keep the authentication payload to pass it to
        // microservices decoded.
        req.context = {
            authPayload: authPayload
        };

        serviceDispatch(req, res);
    });
});

logger.info("Listening on port 3000");
server.listen(3000);
