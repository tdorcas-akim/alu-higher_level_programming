#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (!error) {
    const todos = JSON.parse(body);
    const completedTasks = {};

    for (const task of todos) {
      if (task.completed) {
        const userId = task.userId;
        if (completedTasks[userId]) {
          completedTasks[userId]++;
        } else {
          completedTasks[userId] = 1;
        }
      }
    }

    console.log(completedTasks);
  } else {
    console.log(error);
  }
});
