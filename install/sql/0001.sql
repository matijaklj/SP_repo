BEGIN;
--
-- Create model Follow
--
CREATE TABLE "microblog_web_follow" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT);
--
-- Create model Post
--
CREATE TABLE "microblog_web_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content" text NOT NULL, "post_date" date NOT NULL);
--
-- Create model User
--
CREATE TABLE "microblog_web_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_name" varchar(30) NOT NULL, "description" varchar(100) NOT NULL);
--
-- Add field user to post
--
ALTER TABLE "microblog_web_post" RENAME TO "microblog_web_post__old";
CREATE TABLE "microblog_web_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content" text NOT NULL, "post_date" date NOT NULL, "user_id" integer NOT NULL REFERENCES "microblog_web_user" ("id"));
INSERT INTO "microblog_web_post" ("id", "user_id", "post_date", "content") SELECT "id", NULL, "post_date", "content" FROM "microblog_web_post__old";
DROP TABLE "microblog_web_post__old";
CREATE INDEX "microblog_web_post_e8701ad4" ON "microblog_web_post" ("user_id");
--
-- Add field user1 to follow
--
ALTER TABLE "microblog_web_follow" RENAME TO "microblog_web_follow__old";
CREATE TABLE "microblog_web_follow" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user1_id" integer NOT NULL REFERENCES "microblog_web_user" ("id"));
INSERT INTO "microblog_web_follow" ("id", "user1_id") SELECT "id", NULL FROM "microblog_web_follow__old";
DROP TABLE "microblog_web_follow__old";
CREATE INDEX "microblog_web_follow_91b375bd" ON "microblog_web_follow" ("user1_id");
--
-- Add field user2 to follow
--
ALTER TABLE "microblog_web_follow" RENAME TO "microblog_web_follow__old";
CREATE TABLE "microblog_web_follow" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user1_id" integer NOT NULL REFERENCES "microblog_web_user" ("id"), "user2_id" integer NOT NULL REFERENCES "microblog_web_user" ("id"));
INSERT INTO "microblog_web_follow" ("id", "user1_id", "user2_id") SELECT "id", "user1_id", NULL FROM "microblog_web_follow__old";
DROP TABLE "microblog_web_follow__old";
CREATE INDEX "microblog_web_follow_91b375bd" ON "microblog_web_follow" ("user1_id");
CREATE INDEX "microblog_web_follow_18dfed30" ON "microblog_web_follow" ("user2_id");
COMMIT;

