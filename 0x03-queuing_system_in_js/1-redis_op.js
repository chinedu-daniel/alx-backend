#!/usr/bin/node

import { createClient, print } from 'redis';

// Create a Redis client
const client = createClient();

// Handle connection error
client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

// Handle connection success
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
      if (!err)
        console.log(reply);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
