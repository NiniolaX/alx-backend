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

// Publish a message to channel after delay
const CHANNEL = "holberton school channel";

function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish(CHANNEL, message);
  }, time);
};

// Schedule messages
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
