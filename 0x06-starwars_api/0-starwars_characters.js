#!/usr/bin/node

function findCharacter (index, url, characters, bound) {
  if (index === bound) {
    return;
  }
  request(url, function (error, response, body) {
    if (!error) {
      const character = JSON.parse(body);
      console.log(character.name);
      index++;
      findCharacter(index, characters[index], characters, bound);
    } else {
      console.error('error:', error);
    }
  });
}

const argv = process.argv;

const request = require('request');

request(`https://swapi-api.hbtn.io/api/films/${argv[2]}`,
  function (error, response, body) {
    if (!error) {
      const filmBody = JSON.parse(body);
      const characters = filmBody.characters;

      if (characters !== null && characters.length > 0) {
        const bound = characters.length;
        findCharacter(0, characters[0], characters, bound);
      }
    } else {
      console.log(error);
    }
  });
