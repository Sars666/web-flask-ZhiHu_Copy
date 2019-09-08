DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS question;
DROP TABLE IF EXISTS answer;

CREATE TABLE user (
  userID   INTEGER      NOT NULL PRIMARY KEY AUTOINCREMENT,
  username VARCHAR(45)  NOT NULL UNIQUE      DEFAULT '',
  password VARCHAR(128) NOT NULL             DEFAULT '',
  headUrl  TEXT         NOT NULL             DEFAULT '/static/img/default_head.jpg',
  nickname VARCHAR(256) NOT NULL             DEFAULT 'User',
  sign     TEXT         NOT NULL             DEFAULT '请用一句简单的话描述自己'
);

CREATE TABLE question (
  questionID   INTEGER   NOT NULL PRIMARY KEY AUTOINCREMENT,
  title        TEXT      NOT NULL UNIQUE ,
  detail       TEXT      NOT NULL             DEFAULT '',
  created      TIMESTAMP NOT NULL             DEFAULT CURRENT_TIMESTAMP,
  commentCount INTEGER   NOT NULL             DEFAULT 0,
  topic        TEXT      NOT NULL             DEFAULT '',
  views        INTEGER   NOT NULL             DEFAULT 0,
  followers    INTEGER   NOT NULL             DEFAULT 0
);

CREATE TABLE answer (
  answerID   INTEGER   NOT NULL PRIMARY KEY AUTOINCREMENT,
  userID     INTEGER   NOT NULL             DEFAULT 0,
  questionID INTEGER   NOT NULL             DEFAULT 0,
  answer     TEXT      NOT NULL             DEFAULT '',
  created    TIMESTAMP NOT NULL             DEFAULT CURRENT_TIMESTAMP,
  upvote     INTEGER   NOT NULL             DEFAULT 0,
  downvote   INTEGER   NOT NULL             DEFAULT 0,
  commentCount INTEGER   NOT NULL             DEFAULT 0,
  FOREIGN KEY (userID) REFERENCES user (userID),
  FOREIGN KEY (questionID) REFERENCES question (questionID)
);