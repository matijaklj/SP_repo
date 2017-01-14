BEGIN;
--
-- Add field location_lat to post
--
ALTER TABLE "microblog_web_post" RENAME TO "microblog_web_post__old";
CREATE TABLE "microblog_web_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "location_lat" decimal NULL, "content" text NOT NULL, "pub_date" datetime NOT NULL, "profile_id" integer NOT NULL REFERENCES "microblog_web_profile" ("id"));
INSERT INTO "microblog_web_post" ("id", "pub_date", "content", "profile_id", "location_lat") SELECT "id", "pub_date", "content", "profile_id", NULL FROM "microblog_web_post__old";
DROP TABLE "microblog_web_post__old";
CREATE INDEX "microblog_web_post_83a0eb3f" ON "microblog_web_post" ("profile_id");
--
-- Add field location_lon to post
--
ALTER TABLE "microblog_web_post" RENAME TO "microblog_web_post__old";
CREATE TABLE "microblog_web_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content" text NOT NULL, "pub_date" datetime NOT NULL, "profile_id" integer NOT NULL REFERENCES "microblog_web_profile" ("id"), "location_lat" decimal NULL, "location_lon" decimal NULL);
INSERT INTO "microblog_web_post" ("pub_date", "location_lat", "profile_id", "id", "content", "location_lon") SELECT "pub_date", "location_lat", "profile_id", "id", "content", NULL FROM "microblog_web_post__old";
DROP TABLE "microblog_web_post__old";
CREATE INDEX "microblog_web_post_83a0eb3f" ON "microblog_web_post" ("profile_id");
COMMIT;
