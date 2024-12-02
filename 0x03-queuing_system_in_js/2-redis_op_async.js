// Tests connection to redis server
import redis from 'redis';
import { promisify } from 'util';

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

// Promisify get method of redis client
const clientGetAsync = promisify(client.get).bind(client);

// Function to set a new school value
function setNewSchool (schoolName, value) {
  client.set(schoolName, value, redis.print);
};

// Function to get a school value
async function displaySchoolValue (schoolName) {
  try {
    const value = await clientGetAsync(schoolName);
    if (value) {
      console.log(value);
    }
  } catch (err) {
    console.log(err);
  }
};

// Test functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
