ETL-процесс распределенной обработки данных с помошью PySpark

Цель: разработка приложения по извлечению данных, их преобразованию и загрузке в целевую систему.
Этапы: 
1) парсинг данных по API (В результате парсинга данных с сайта https://dev.to/ будут получены два файла с данными articles.json
и videos.json)
2) разворачивание hdfs и доставка полученных на предыдущем этапе данных
3) обработка данных на PySpark
4) разворачивание Postgres и запись предобрабтанных данных
5) построение дашборда в Superset

Технологии:
1) REST API
2) распределенная файловая система HDFS
3) фреймворк обработки больших данных PySpark
4) база данных PostgreSQL
5) Docker compose
6) платформа для визуализации данных Superset

Проект написан на Python с использованием Jupyter notebook.
Все компоненты приложения, за исключением PostgreSQL, разворачивается из Docker-контейнеров.

Системные требования:
- Docker compose
- Postgres 17


Структура приложения:
- docker-compose.yml - конфигурационный файл для запуска контейнеров
- PP_articles_parsing.py - функция парсинга данных по REST API
- Pyspark_job_articles.ipnb - jupyter-блокнот с обработкой данных на PySpark
- hadoop.env - переменные окружения hdfs
- superset.env - переменные окружения superset
- dashboard_export_20250624T103946.zip - файл с экспортированным из Superset дашбордом

Хосты: 
- http://localhost:8088/ - Superset
- http://localhost:8888/ - Jupyter Notebook
- http://localhost:9870/ - Hadoop


Инструкция по разворачиванию приложения:

1) парсим данные с сайта dev.to
`python3 PP_articles_parsing.py`
Теперь в корневой папке появятся два файла с данными: articles.json и videos.json
2) запускаем docker-compose
`docker-compose up`
5) переходим в UI Hadoop - http://localhost:9870/ - у нас есть одна namenode и три datanode, сейчас они пустые
6) складываем в namemode в корень файлы articles.json и videos.json
docker cp articles.json namenode:/
docker cp videos.json namenode:/
7) подключаемся к контейнеру с namenode
docker exec -it namenode /bin/bash
просматриваем содержимое
ls  
8) положим файлы в hadoop в корень
hdfs dfs -put articles.json /
hdfs dfs -put videos.json /
9) проверим, что файлы есть в hadoop (http://localhost:9870/) - вкладка Utilities - Browse the file system
10) зайдем в юпитер ноутбук по адресу http://localhost:8888/
11) переходим в папку notebooks, открываем файл Pyspark_job_articles.ipynb
12) теперь в локальном PostgreSQL появится схема pp_articles с таблицами
13) перейдем в UI Superset - http://localhost:8088/
14) импортируем предварительно созданный дашборд: вкладка Dashboards - Import Dashboard (в верхнем правом углу) - выюираем файл dashboard_export_20250624T103946.zip из нашего репозитория 

 



 
