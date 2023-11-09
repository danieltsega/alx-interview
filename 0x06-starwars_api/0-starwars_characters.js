#!/usr/bin/node

const request = require('request');

// Get Movie ID from Command Line
const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

// Make API Request
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error(`Error: Unable to fetch data. Status Code: ${response ? response.statusCode : 'Unknown'}`);
    process.exit(1);
  }

  // Extract Characters
  const characters = JSON.parse(body).characters;

  // Display Characters Sequentially
  displayCharactersSequentially(characters);
});

// Display Characters Sequentially
function displayCharactersSequentially (characters) {
  const index = 0;

  function fetchCharacter (index) {
    if (index >= characters.length) {
      // All characters fetched, exit the process
      process.exit(0);
    }

    const characterUrl = characters[index];
    request(characterUrl, (error, response, body) => {
      if (error || response.statusCode !== 200) {
        console.error(`Error fetching character: ${error ? error.message : 'Unknown'}`);
      } else {
        console.log(JSON.parse(body).name);
      }

      // Fetch the next character
      fetchCharacter(index + 1);
    });
  }

  // Start fetching characters
  fetchCharacter(index);
}
