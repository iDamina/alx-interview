#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const movieEndpoint = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

if (!movieId) {
  console.error('Usage: node script.js <Movie ID>');
  process.exit(1);
}

function fetchCharacterName(url, callback) {
  request(url, (error, response, body) => {
    if (error) {
      callback(error, null);
      return;
    }

    if (response.statusCode !== 200) {
      const errorMsg = `Failed to fetch ${url}: ${response.statusMessage}`;
      callback(new Error(errorMsg), null);
      return;
    }

    const character = JSON.parse(body).name;
    callback(null, character);
  });
}

function fetchCharacters(characterList, index = 0) {
  if (index >= characterList.length) {
    return;
  }

  fetchCharacterName(characterList[index], (error, name) => {
    if (error) {
      console.error(error.message);
    } else {
      console.log(name);
      fetchCharacters(characterList, index + 1);
    }
  });
}

request(movieEndpoint, (error, response, body) => {
  if (error) {
    console.error(`Error fetching movie data: ${error.message}`);
    return;
  }

  if (response.statusCode !== 200) {
    const errorMsg = `Failed to fetch movie data: ${response.statusMessage}`;
    console.error(new Error(errorMsg).message);
    return;
  }

  const characterList = JSON.parse(body).characters;
  fetchCharacters(characterList);
});
