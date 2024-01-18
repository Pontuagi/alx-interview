#!/usr/bin/node

/*
 * Starwars APi module
 * A script that prints all characters of a Star Wars movie
 */

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

if (movieId < 1 || movieId > 7) {
  console.log('Invalid Movie Id');
  process.exit(1);
}
request(url, async function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      const characterName = await new Promise((resolve, reject) => {
        request(character, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      });
      console.log(characterName);
    }
  }
});
