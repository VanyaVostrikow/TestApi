CREATE TABLE "CategoriesOfProducts" (
  "id" int PRIMARY KEY,
  "name" varchar UNIQUE NOT NULL,
  "seq" int NOT NULL
);

CREATE TABLE "GroupsOfProducts" (
  "id" uuid PRIMARY KEY,
  "category_id" int,
  "name" varchar UNIQUE NOT NULL,
  "description" varchar,
  "seq" int NOT NULL
);

CREATE TABLE "Products" (
  "id" uuid PRIMARY KEY,
  "group_id" uuid,
  "name" varchar UNIQUE NOT NULL,
  "price" double precision,
  "hidden" boolean DEFAULT false
);

ALTER TABLE "GroupsOfProducts" ADD FOREIGN KEY ("category_id") REFERENCES "CategoriesOfProducts" ("id");

ALTER TABLE "Products" ADD FOREIGN KEY ("group_id") REFERENCES "GroupsOfProducts" ("id");
