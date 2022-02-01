#!/usr/bin/node
const request = require('request');

if (process.argv.length > 2) {
  const charId = 'https://swapi-api.hbtn.io/api/people/18/';

  request(`${process.argv[2]}`, (err, res, body) => {
    if (err) {
      console.log(err);
    }
    const films = JSON.parse(body).results;
    const charFilms = films.filter(x => x.characters.includes(charId));

    console.log(charFilms.length);
  });
}
