#Welcome to the Data Engineering challenge.

As a data engineer, it's often the case that data lies distributed all over the ecosystem of the organization.
In our case we get data from different APIs as well as Sales systems (like Salesforce) or other SAAS tools
the company is using.

Our Head of Demand generation is interested in analyzing the last tweets of specific persons, 
he wrote a magic script which runs in psql and therefore the text of the tweet needs to be accessible in the datalake.

The goal is to fetch n tweets for a given username x and dump them into
the data lake, so our analysts can play with it. For this exercise please use postgres as the RDBS.


Task:
- Write a small tool in the language of your choice, that accepts a twitter username as a parameter 
  and fetches the last 5 tweets of that user.
  A sample call could be:
    `./fetch --user UserName`

- Persistence is one of the main points.
  Postgres would be the first coice, but you can use any RDBS you want.
  Elaborate for a second what the "MVP" of information is which you need to persist.
  (Pick the basics things to be able to indentify the tweet and the emitter etc)
  
- Investigate the Twitter data model and think about how things are related there
-- How would you model hastag / tweet / followers and what is the best data structure to model that,
   it won't harm to put some of that into your example code :)

- Check your code into Github and sent the link before you come onside



Here are some twitter credentials to get you started:

Twitter consumer key
  `t8bhToaY4LevkBjvS355A9pfu`
Twitter consumer secret
  `2315cTZYr7OQmoDytBWpuothCAakOYER7pE6fF3ZLUXeAC8rkz`

Twitter access token
  `882165583911038976-XgiJxECv0cCsg2Ech6HmzPuzsD1zILp`
Twitter access token secret
  `e9puaP5NBK0JWjEUXCE214yc2CXpkgC1zPMzmgDs5ZLc5`


Bonus (let's see what we can do more!):
- use an ORM
- schema migrations
- build any sql aggregate and display result after persisting

