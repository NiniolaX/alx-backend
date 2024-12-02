// Tests connection to redis server
import redis from 'redis';

// Create a new client
const client = redis.createClient();

// Listen for error event
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Listen for connect event
client.on('connect', () => {
  console.log('Redis client connected to the server');
});
