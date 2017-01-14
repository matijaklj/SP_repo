BEGIN;
--
-- Alter field coverImage on profile
--
ALTER TABLE "microblog_web_profile" RENAME TO "microblog_web_profile__old";
CREATE TABLE "microblog_web_profile" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "coverImage" varchar(100) NOT NULL, "description" varchar(150) NOT NULL, "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "displayName" varchar(30) NOT NULL, "profileImage" varchar(100) NOT NULL);
INSERT INTO "microblog_web_profile" ("id", "displayName", "coverImage", "profileImage", "description", "user_id") SELECT "id", "displayName", "coverImage", "profileImage", "description", "user_id" FROM "microblog_web_profile__old";
DROP TABLE "microblog_web_profile__old";
CREATE INDEX "microblog_web_profile_e8701ad4" ON "microblog_web_profile" ("user_id");
--
-- Alter field profileImage on profile
--
ALTER TABLE "microblog_web_profile" RENAME TO "microblog_web_profile__old";
CREATE TABLE "microblog_web_profile" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "description" varchar(150) NOT NULL, "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "displayName" varchar(30) NOT NULL, "coverImage" varchar(100) NOT NULL, "profileImage" varchar(100) NOT NULL);
INSERT INTO "microblog_web_profile" ("id", "displayName", "coverImage", "profileImage", "description", "user_id") SELECT "id", "displayName", "coverImage", "profileImage", "description", "user_id" FROM "microblog_web_profile__old";
DROP TABLE "microblog_web_profile__old";
CREATE INDEX "microblog_web_profile_e8701ad4" ON "microblog_web_profile" ("user_id");
COMMIT;
