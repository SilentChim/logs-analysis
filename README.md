# logs-analysis
Reporting tool that prints out reports (in plain text) based on the data in the database

1. Open Terminal

2. Download and install the VM configuration
    - Navigate to the directory via: cd Downloads/fsnd-virtual-machine

3. Download the database
    - Download the data at this address: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
    - Put this file into the vagrant directory, which is shared with your virtual machine

3. Start the virtual machine
    - Type ‘vagrant up’ into the command line

4. Connect to the virtual machine
    - Type ‘vagrant ssh’ into the command line

5. Once connected, find the files for running the tests
    - Type ‘cd /vagrant’ to navigate to the directory containing the files, and type ‘ls’
      to list the files in the vagrant directory.
    - Navigate to the logs_analysis folder inside the vagrant directory: type ‘cd logs_analysis’
    - Type ‘ls’ to list the files in the logs_analysis directory

6. Once logs_analysis directory files are listed, select the newsdata.py file
    - Type ‘python newsdata.py’ to execute the test file.

7. CREATE VIEW statements listed below:
      CREATE VIEW top_articles AS
      SELECT
      articles.title,
      COUNT(log.time) AS views
      FROM articles
      JOIN log ON log.path LIKE concat('%',articles.slug)
      GROUP BY articles.title
      ORDER BY views DESC
      LIMIT 3;

      CREATE VIEW top_authors AS
      SELECT
      authors.name,
      COUNT(log.time) AS views
      FROM articles
      JOIN log ON log.path LIKE concat('%',articles.slug)
      JOIN authors ON authors.id = articles.author
      GROUP BY authors.name
      ORDER BY views DESC
      LIMIT 4;

      CREATE VIEW request_errors AS
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
        (errors.status_errors*1.0) / total.status_totals) * 100, 1) > 1;
