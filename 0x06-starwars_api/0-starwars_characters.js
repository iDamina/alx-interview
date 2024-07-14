#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const movieEndpoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

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
      callback(`Failed to fetch ${url}: ${response.statusMessage}`, null);
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
      console.error(error);
    } else {
      console.log(name);
      fetchCharacters(characterList, index + 1);
    }
  });
}

request(movieEndpoint, (error, response, body) => {
  if (error) {
    console.error(`Error fetching movie data: ${error}`);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie data: ${response.statusMessage}`);
    return;
  }

  const characterList = JSON.parse(body).characters;
  fetchCharacters(characterList);
});
