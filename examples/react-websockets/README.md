# Reactive Webapp

This example implements a simple Express based server to receive events from gridX through webhooks.
It forwards each events to a client app using websockets, to implement a fully reactive pattern instead of relying on polling.

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