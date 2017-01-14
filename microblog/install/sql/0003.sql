BEGIN;
--
-- Remove field user from post
--
ALTER TABLE "microblog_web_post" RENAME TO "microblog_web_post__old";
CREATE TABLE "microblog_web_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content" text NOT NULL, "pub_date" date NOT NULL);
INSERT INTO "microblog_web_post" ("pub_date", "id", "content") SELECT "pub_date", "id", "content" FROM "microblog_web_post__old";
DROP TABLE "microblog_web_post__old";
--
-- Add field profile to post
--
ALTER TABLE "microblog_web_post" RENAME TO "microblog_web_post__old";
CREATE TABLE "microblog_web_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "profile_id" integer NOT NULL REFERENCES "microblog_web_profile" ("id"), "content" text NOT NULL, "pub_date" date NOT NULL);
INSERT INTO "microblog_web_post" ("pub_date", "profile_id", "id", "content") SELECT "pub_date", 2, "id", "content" FROM "microblog_web_post__old";
DROP TABLE "microblog_web_post__old";
CREATE INDEX "microblog_web_post_83a0eb3f" ON "microblog_web_post" ("profile_id");
--
-- Add field displayName to profile
--
ALTER TABLE "microblog_web_profile" RENAME TO "microblog_web_profile__old";
CREATE TABLE "microblog_web_profile" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "description" varchar(100) NOT NULL, "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "displayName" varchar(30) NOT NULL);
INSERT INTO "microblog_web_profile" ("description", "id", "user_id", "displayName") SELECT "description", "id", "user_id", 'makaka' FROM "microblog_web_profile__old";
DROP TABLE "microblog_web_profile__old";
CREATE INDEX "microblog_web_profile_e8701ad4" ON "microblog_web_profile" ("user_id");
--
-- Alter field description on profile
--
ALTER TABLE "microblog_web_profile" RENAME TO "microblog_web_profile__old";
CREATE TABLE "microblog_web_profile" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "displayName" varchar(30) NOT NULL, "description" varchar(150) NOT NULL);
INSERT INTO "microblog_web_profile" ("description", "id", "user_id", "displayName") SELECT "description", "id", "user_id", "displayName" FROM "microblog_web_profile__old";
DROP TABLE "microblog_web_profile__old";
CREATE INDEX "microblog_web_profile_e8701ad4" ON "microblog_web_profile" ("user_id");
COMMIT;
