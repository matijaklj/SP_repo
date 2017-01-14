BEGIN;
--
-- Alter field name on hashtag
--
ALTER TABLE "microblog_web_hashtag" RENAME TO "microblog_web_hashtag__old";
CREATE TABLE "microblog_web_hashtag" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL UNIQUE);
INSERT INTO "microblog_web_hashtag" ("name", "id") SELECT "name", "id" FROM "microblog_web_hashtag__old";
DROP TABLE "microblog_web_hashtag__old";
--
-- Alter field pub_date on post
--
ALTER TABLE "microblog_web_post" RENAME TO "microblog_web_post__old";
CREATE TABLE "microblog_web_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content" text NOT NULL, "profile_id" integer NOT NULL REFERENCES "microblog_web_profile" ("id"), "pub_date" datetime NOT NULL);
INSERT INTO "microblog_web_post" ("pub_date", "profile_id", "id", "content") SELECT "pub_date", "profile_id", "id", "content" FROM "microblog_web_post__old";
DROP TABLE "microblog_web_post__old";
CREATE INDEX "microblog_web_post_83a0eb3f" ON "microblog_web_post" ("profile_id");
COMMIT;
