import redis, { createClient } from 'redis';

// Create redis client
const client = createClient();

// Check connection
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Subscribe to channel
const CHANNEL = 'holberton school channel';
client.subscribe(CHANNEL);

client.on('message', (channel, message) => {
  console.log(message);
  if (message === "KILL_SERVER") {
    client.unsubscribe(channel);
    client.quit();
  }
});
