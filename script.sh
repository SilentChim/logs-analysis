#!/bin/bash
echo "running script"
echo "Populating database..."
psql -d news -f newsdata.sql
echo "What are the most popular three articles of all time?"
psql -d news -c "CREATE OR REPLACE VIEW top_articles AS
  SELECT
    articles.title,
    COUNT(log.time) AS views
  FROM articles
    JOIN log ON log.path LIKE concat('%',articles.slug)
  GROUP BY articles.title
  ORDER BY views DESC
  LIMIT 3;"
psql -d news -c "SELECT * FROM top_articles;"

echo "Who are the most popular article authors of all time?"
psql -d news -c "CREATE OR REPLACE VIEW top_authors AS
  SELECT
    authors.name,
    COUNT(log.time) AS views
  FROM articles
    JOIN log ON log.path LIKE concat('%',articles.slug)
    JOIN authors ON authors.id = articles.author
  GROUP BY authors.name
  ORDER BY views DESC
  LIMIT 4;"
psql -d news -c "SELECT * FROM top_authors;"

echo "On which days did more than 1% of requests lead to errors?"
psql -d news -c "CREATE OR REPLACE VIEW request_errors AS
  WITH errors AS (
    SELECT time::date AS date, COUNT(*) AS status_errors
    FROM log WHERE log.status != '200 OK'
    GROUP BY log.time::date
    ),
    total AS (
    SELECT time::date AS date, COUNT(*) AS status_totals
    FROM log
    GROUP BY time::date
    )
    SELECT errors.date, round( (
      (errors.status_errors*1.0) / total.status_totals) * 100, 1)
    FROM errors, total WHERE errors.date = total.date AND round( (
      (errors.status_errors*1.0) / total.status_totals) * 100, 1) > 1;"
psql -d news -c "SELECT * FROM request_errors;"
