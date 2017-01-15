BEGIN;
--
-- Add field date to post_hashtag
--
ALTER TABLE "microblog_web_post_hashtag" RENAME TO "microblog_web_post_hashtag__old";
CREATE TABLE "microblog_web_post_hashtag" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "date" datetime NOT NULL, "hashtag_id" integer NOT NULL REFERENCES "microblog_web_hashtag" ("id"), "post_id" integer NOT NULL REFERENCES "microblog_web_post" ("id"));
INSERT INTO "microblog_web_post_hashtag" ("date", "post_id", "id", "hashtag_id") SELECT '2017-01-14 16:39:48.037715', "post_id", "id", "hashtag_id" FROM "microblog_web_post_hashtag__old";
DROP TABLE "microblog_web_post_hashtag__old";
CREATE INDEX "microblog_web_post_hashtag_e4858d5c" ON "microblog_web_post_hashtag" ("hashtag_id");
CREATE INDEX "microblog_web_post_hashtag_f3aa1999" ON "microblog_web_post_hashtag" ("post_id");
COMMIT;
