// Adds hash to database using redis client
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

// Create hash
const KEY = 'HolbertonSchools';
const data = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2,
};

for (const [field, value] of Object.entries(data)) {
  client.hset(KEY, field, value, redis.print);
};

// Display hash
client.hgetall('HolbertonSchools', (err, hash) => {
  if (err) {
    console.error(`Error fetching hash: ${err.message}`);
  } else {
    console.log(hash);
  }
});
