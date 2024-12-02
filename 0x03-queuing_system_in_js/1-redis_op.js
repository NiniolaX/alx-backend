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

// Function to set a new school value
function setNewSchool (schoolName, value) {
  client.set(schoolName, value, redis.print);
};

// Function to get a school value
function displaySchoolValue (schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.log(err);
    } else {
      console.log(reply); // Logs the value of the key
    }
  });
};

// Test functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
