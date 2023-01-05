# 2023 Heroku Deployment Instructions for Node/Express or MERN-Stack Applications

## Notice:

- this guide assumes you have a heroku URL already:
- if you don't have one, follow these steps:
  - `cd` into your project repo
  - run `heroku login` to activate the heroku CLI
  - create a new app on Heroku by running `heroku create` on the root level of your project
  - confirm that the Heroku app is created by running `git remote -v`
    - you should see a new remote called `heroku`. this will be made for you automatically

## What needs to be updated?

- create a new folder called `bin` and make a new file called: `www` (no file type needed) inside your project's root folder
  - this file may be already existing if you started your project with `express-generator`
- set `bin/www` to have this content:
  - pay special attention to `var debug = require("debug")("YOUR APP NAME GOES HERE:server");` DO NOT FORGET TO SWITCH IN YOUR APP'S NAME AS DEFINED ON HEROKU

```js
#!/usr/bin/env node

/**
 * Module dependencies.
 */

var app = require("../server");
var debug = require("debug")("YOUR APP GOES HERE:server");
var http = require("http");

/**
 * Get port from environment and store in Express.
 */

var port = normalizePort(process.env.PORT || "3000");
app.set("port", port);

/**
 * Create HTTP server.
 */

var server = http.createServer(app);

/**
 * Listen on provided port, on all network interfaces.
 */

server.listen(port);
server.on("error", onError);
server.on("listening", onListening);

/**
 * Normalize a port into a number, string, or false.
 */

function normalizePort(val) {
  var port = parseInt(val, 10);

  if (isNaN(port)) {
    // named pipe
    return val;
  }

  if (port >= 0) {
    // port number
    return port;
  }

  return false;
}

/**
 * Event listener for HTTP server "error" event.
 */

function onError(error) {
  if (error.syscall !== "listen") {
    throw error;
  }

  var bind = typeof port === "string" ? "Pipe " + port : "Port " + port;

  // handle specific listen errors with friendly messages
  switch (error.code) {
    case "EACCES":
      console.error(bind + " requires elevated privileges");
      process.exit(1);
      break;
    case "EADDRINUSE":
      console.error(bind + " is already in use");
      process.exit(1);
      break;
    default:
      throw error;
  }
}

/**
 * Event listener for HTTP server "listening" event.
 */

function onListening() {
  var addr = server.address();
  var bind = typeof addr === "string" ? "pipe " + addr : "port " + addr.port;
  debug("Listening on " + bind);
}
```

- delete the bottom part of `server.js`
  - remove anything that has to do with `app.listen` and setting .PORT values
    - look for `const port = process.env`. delete everything below and including this line!
  - you can also remove any middleware and imports relating to CORS from `server.js`
- add `module.exports = app` to the very bottom of `server.js`
- inside `src/utilities/send-request.js`:
  - get rid of code having to do with checking production environments
  - remove the Heroku Base URL if you have one, you can start with fetching from `/ROUTE GOES HERE` instead
  - remove anything relating to code (most likely in your fetch options object)
- inside `package.json`:
  - remove `gh-pages` if you previously tried to deploy your front-end to GH Pages from `devDependencies`
  - remove `gh pages` predeploy from `scripts`
  - remove `homepage: SOME URL GOES HERE` field
  - add `"start": "node ./bin/www"` to `scripts` field
- make a commit to save all these changes!
- run `npm run build` to create a compiled version of your react front end!
- run `git push origin BRANCH` to push up to Github (most likely main branch)

## How to get a MERN-Stack App deployed:

- run `git push heroku main` to push to your heroku URL
- watch deployment build out
  - if any issues, run `heroku logs --tail` to see what went wrong
  - otherwise it will be succesful!
  - it may take 15-20 minutes for your deployment to build itself out! Be patient!
- set config variables online using heroku's dashboard (copy/paste values from .env)