# NodeJS/Express gridX Webhook Receiver Sample

This example implements a simple Express based server to receive events from gridX through webhooks.
It implements only the `appliance/online` event handler.

The implementation just prints some of the received event's data to the console.
You can play around with the server implementation while running it, every change will restart the server.

## Prerequisites

To run this server, you need to have `NodeJS` and `yarn` or `npm` installed.

## Usage

_yarn_
```sh
yarn
yarn start
```

_npm_
```sh
npm install
npm run start
```