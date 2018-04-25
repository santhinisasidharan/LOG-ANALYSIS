# Log- Analysis
https://www.tutorialspoint.com/postgresql/postgresql_python.htm
  This project is made as a part of 3rd project of Udacity full stack nanodegree program. Here we build an internal reporting tool,**reporting_tool.py** that uses information from the database to discover what kind of articles the site's readers like.The database contains information about newspaper articles in 2 tables **authors** and **articles**, and a table **log** for web server log for the site. The log has a database row for each time a reader loaded a web page. The program will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

## Pre- requisites
1. Python 2.7 is required to view the code.
2. Follow [these instructions to install the virtual machine](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0).We're using tools called Vagrant and VirtualBox to install and manage the VM. This will give you the PostgreSQL database and support software needed for this project.
3. The program will run from the command line.
4. Download the database [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Copy to vagrant directory.

## How to run log- analysis?
After installing the softwares mentioned above and the database, follow these instruction to run log analysis.
1. Click on the green color button on repository to clone or download the git repository to your computer.Unpack the zip file.
2. Copy the folder to vagrant directory.
3. Open the console- Terminal for mac and linux, Command prompt for windows.
4. Start the virtual machine as per instructions in installation page.
5. Load the database using `psql -d news -f newsdata.sql`
6. Create views with the following SQL.

`CREATE VIEW article_views AS SELECT path, count(*) AS views FROM log WHERE status='200 OK' AND path LIKE '/article/%' GROUP BY path ORDER BY views DESC;`

`CREATE VIEW popular_article_details AS SELECT author, title, views FROM article_views JOIN articles ON path LIKE CONCAT('%', slug);`

`CREATE VIEW popular_authors AS SELECT name , SUM(views) AS total_views FROM popular_article_details, authors WHERE popular_article_details.author = authors.id GROUP BY name ORDER BY total_views DESC;`

`CREATE VIEW error_log AS SELECT date(time),COUNT(*) AS total_count, COUNT(CASE WHEN status='404 NOT FOUND'THEN 1 END) AS error_count FROM log  GROUP BY date(time);`

`CREATE VIEW percent_error_table AS SELECT date, (CAST(error_count AS DECIMAL)/CAST(total_count AS DECIMAL)*100) AS percentage_error FROM error_log WHERE error_count>(total_count/100);`

7. Run python reporting_tool.py
