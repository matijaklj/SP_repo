BEGIN;
--
-- Remove field user1 from follow
--
ALTER TABLE "microblog_web_follow" RENAME TO "microblog_web_follow__old";
CREATE TABLE "microblog_web_follow" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user2_id" integer NOT NULL REFERENCES "auth_user" ("id"));
INSERT INTO "microblog_web_follow" ("user2_id", "id") SELECT "user2_id", "id" FROM "microblog_web_follow__old";
DROP TABLE "microblog_web_follow__old";
CREATE INDEX "microblog_web_follow_18dfed30" ON "microblog_web_follow" ("user2_id");
--
-- Remove field user2 from follow
--
ALTER TABLE "microblog_web_follow" RENAME TO "microblog_web_follow__old";
CREATE TABLE "microblog_web_follow" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT);
INSERT INTO "microblog_web_follow" ("id") SELECT "id" FROM "microblog_web_follow__old";
DROP TABLE "microblog_web_follow__old";
--
-- Remove field hashtag from post_hashtag
--
ALTER TABLE "microblog_web_post_hashtag" RENAME TO "microblog_web_post_hashtag__old";
CREATE TABLE "microblog_web_post_hashtag" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "post_id" integer NOT NULL REFERENCES "microblog_web_post" ("id"), "date" datetime NOT NULL);
INSERT INTO "microblog_web_post_hashtag" ("post_id", "date", "id") SELECT "post_id", "date", "id" FROM "microblog_web_post_hashtag__old";
DROP TABLE "microblog_web_post_hashtag__old";
CREATE INDEX "microblog_web_post_hashtag_f3aa1999" ON "microblog_web_post_hashtag" ("post_id");
--
-- Remove field post from post_hashtag
--
ALTER TABLE "microblog_web_post_hashtag" RENAME TO "microblog_web_post_hashtag__old";
CREATE TABLE "microblog_web_post_hashtag" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "date" datetime NOT NULL);
INSERT INTO "microblog_web_post_hashtag" ("date", "id") SELECT "date", "id" FROM "microblog_web_post_hashtag__old";
DROP TABLE "microblog_web_post_hashtag__old";
--
-- Add field hashtags to post
--
CREATE TABLE "microblog_web_post_hashtags" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "post_id" integer NOT NULL REFERENCES "microblog_web_post" ("id"), "hashtag_id" integer NOT NULL REFERENCES "microblog_web_hashtag" ("id"));
--
-- Add field following to profile
--
CREATE TABLE "microblog_web_profile_following" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "from_profile_id" integer NOT NULL REFERENCES "microblog_web_profile" ("id"), "to_profile_id" integer NOT NULL REFERENCES "microblog_web_profile" ("id"));
--
-- Delete model Follow
--
DROP TABLE "microblog_web_follow";
--
-- Delete model post_hashtag
--
DROP TABLE "microblog_web_post_hashtag";
CREATE UNIQUE INDEX "microblog_web_post_hashtags_post_id_3aca1e44_uniq" ON "microblog_web_post_hashtags" ("post_id", "hashtag_id");
CREATE INDEX "microblog_web_post_hashtags_f3aa1999" ON "microblog_web_post_hashtags" ("post_id");
CREATE INDEX "microblog_web_post_hashtags_e4858d5c" ON "microblog_web_post_hashtags" ("hashtag_id");
CREATE UNIQUE INDEX "microblog_web_profile_following_from_profile_id_341f8d0f_uniq" ON "microblog_web_profile_following" ("from_profile_id", "to_profile_id");
CREATE INDEX "microblog_web_profile_following_9c2b64df" ON "microblog_web_profile_following" ("from_profile_id");
CREATE INDEX "microblog_web_profile_following_658493f6" ON "microblog_web_profile_following" ("to_profile_id");
COMMIT;
