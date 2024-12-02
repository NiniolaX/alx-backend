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
client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);

// Display hash
client.hgetall('HolbertonSchools', (err, hash) => {
  if (err) {
    console.error(`Error fetching hash: ${err.message}`);
  } else {
    console.log(hash);
  }
});
