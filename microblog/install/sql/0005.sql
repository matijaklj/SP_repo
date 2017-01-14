BEGIN;
--
-- Create model Hashtag
--
CREATE TABLE "microblog_web_hashtag" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL);
--
-- Create model post_hashtag
--
CREATE TABLE "microblog_web_post_hashtag" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "hashtag_id" integer NOT NULL REFERENCES "microblog_web_hashtag" ("id"), "post_id" integer NOT NULL REFERENCES "microblog_web_post" ("id"));
CREATE INDEX "microblog_web_post_hashtag_e4858d5c" ON "microblog_web_post_hashtag" ("hashtag_id");
CREATE INDEX "microblog_web_post_hashtag_f3aa1999" ON "microblog_web_post_hashtag" ("post_id");
COMMIT;
