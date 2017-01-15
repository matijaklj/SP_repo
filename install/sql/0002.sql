BEGIN;
--
-- Create model Profile
--
CREATE TABLE "microblog_web_profile" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "description" varchar(100) NOT NULL);
--
-- Remove field post_date from post
--
ALTER TABLE "microblog_web_post" RENAME TO "microblog_web_post__old";
CREATE TABLE "microblog_web_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content" text NOT NULL, "user_id" integer NOT NULL REFERENCES "microblog_web_user" ("id"));
INSERT INTO "microblog_web_post" ("user_id", "content", "id") SELECT "user_id", "content", "id" FROM "microblog_web_post__old";
DROP TABLE "microblog_web_post__old";
CREATE INDEX "microblog_web_post_e8701ad4" ON "microblog_web_post" ("user_id");
--
-- Add field pub_date to post
--
ALTER TABLE "microblog_web_post" RENAME TO "microblog_web_post__old";
CREATE TABLE "microblog_web_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content" text NOT NULL, "user_id" integer NOT NULL REFERENCES "microblog_web_user" ("id"), "pub_date" date NOT NULL);
INSERT INTO "microblog_web_post" ("content", "id", "pub_date", "user_id") SELECT "content", "id", '2017-01-14', "user_id" FROM "microblog_web_post__old";
DROP TABLE "microblog_web_post__old";
CREATE INDEX "microblog_web_post_e8701ad4" ON "microblog_web_post" ("user_id");
--
-- Alter field user1 on follow
--
ALTER TABLE "microblog_web_follow" RENAME TO "microblog_web_follow__old";
CREATE TABLE "microblog_web_follow" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user2_id" integer NOT NULL REFERENCES "microblog_web_user" ("id"), "user1_id" integer NOT NULL REFERENCES "auth_user" ("id"));
INSERT INTO "microblog_web_follow" ("user2_id", "id", "user1_id") SELECT "user2_id", "id", "user1_id" FROM "microblog_web_follow__old";
DROP TABLE "microblog_web_follow__old";
CREATE INDEX "microblog_web_follow_18dfed30" ON "microblog_web_follow" ("user2_id");
CREATE INDEX "microblog_web_follow_91b375bd" ON "microblog_web_follow" ("user1_id");
--
-- Alter field user2 on follow
--
ALTER TABLE "microblog_web_follow" RENAME TO "microblog_web_follow__old";
CREATE TABLE "microblog_web_follow" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user1_id" integer NOT NULL REFERENCES "auth_user" ("id"), "user2_id" integer NOT NULL REFERENCES "auth_user" ("id"));
INSERT INTO "microblog_web_follow" ("user2_id", "id", "user1_id") SELECT "user2_id", "id", "user1_id" FROM "microblog_web_follow__old";
DROP TABLE "microblog_web_follow__old";
CREATE INDEX "microblog_web_follow_91b375bd" ON "microblog_web_follow" ("user1_id");
CREATE INDEX "microblog_web_follow_18dfed30" ON "microblog_web_follow" ("user2_id");
--
-- Alter field user on post
--
ALTER TABLE "microblog_web_post" RENAME TO "microblog_web_post__old";
CREATE TABLE "microblog_web_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content" text NOT NULL, "pub_date" date NOT NULL, "user_id" integer NOT NULL REFERENCES "auth_user" ("id"));
INSERT INTO "microblog_web_post" ("content", "id", "pub_date", "user_id") SELECT "content", "id", "pub_date", "user_id" FROM "microblog_web_post__old";
DROP TABLE "microblog_web_post__old";
CREATE INDEX "microblog_web_post_e8701ad4" ON "microblog_web_post" ("user_id");
--
-- Delete model User
--
DROP TABLE "microblog_web_user";
--
-- Add field user to profile
--
ALTER TABLE "microblog_web_profile" RENAME TO "microblog_web_profile__old";
CREATE TABLE "microblog_web_profile" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "description" varchar(100) NOT NULL, "user_id" integer NOT NULL REFERENCES "auth_user" ("id"));
INSERT INTO "microblog_web_profile" ("id", "description", "user_id") SELECT "id", "description", NULL FROM "microblog_web_profile__old";
DROP TABLE "microblog_web_profile__old";
CREATE INDEX "microblog_web_profile_e8701ad4" ON "microblog_web_profile" ("user_id");
COMMIT;
