#!/usr/bin/node
// computes the number of completed tasks by id

const request = require('request');
const api = process.argv[2];

request.get(api, (error, response, body) => {
  if (error) return console.error(error);
  const completed = {};
  const todos = JSON.parse(body);
  todos.forEach((todo) => {
    if (todo.completed) {
      if (!completed[todo.userId]) completed[todo.userId] = 1;
      else completed[todo.userId] += 1;
    }
  });
  console.log(completed);
});
