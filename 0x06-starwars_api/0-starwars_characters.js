#!/usr/bin/node

// Starwars API
const argv = process.argv;
const request = require('request');
request(`https://swapi-api.alx-tools.com/api/films/${argv[2]}`,
  function (error, response, body) {
    if (error == null) {
      const filmBody = JSON.parse(body);
      const characters = filmBody.characters;
      //    console.log(characters);
      if (characters && characters.length > 0) {
        let charUrl = '';
        let i = 0;
        for (i; i < characters.length; i++) {
          charUrl = characters[i];
          request(charUrl, function (error, response, body) {
            if (error == null) {
              const characDetail = JSON.parse(body);
              const characName = characDetail.name;
              console.log(characName);
            } else {
              console.log(error);
            }
          });
        }
      }
    } else { console.log('error: ', error); }
  });
