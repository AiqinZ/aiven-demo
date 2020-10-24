Aiven Demo
============
To run this project, please use Python 3.

This is a demo project operating Kafka and Postgresql. There's a Kafka producer and a consumer, and the consumer will write a record into a Postgresql table for every record it receives.

Prerequisites
-------------
Step 1: Download this project from github using ``git-clone``.

Step 2: Create python virtual environment::

  aiven_demo> python -m venv venv

Step3: activate venv::

  On MacOS, run:
  aiven_demo> source venv/bin/activate

  On Windows, run:
  aiven_demo> venv\Scripts\activate.bat

Step 4: Install dependent libraries::

  aiven_demo> pip3 install -r requirements.txt


Set up Kafka
----------------
Set up Kafka for sending and consuming messages. A new topic should be created in Kafka for test purpose to run this project, and you should configure the topic id in the config file named ``config.ini`` or ``config_local.ini`` in this project. The file ``config_local.ini`` is recommended to be used as it's a localized configuration file, you don't have to change ``config.ini`` as it's used as a template.

To make it easy, you can set it up via cloud, such as Aiven online Kafka. Aiven Kafka needs SSL certificate files. After downloading ``ca.pem``, ``service.cert`` and ``service.key`` from Aiven's web console, you need to put them in the root directory of the project, and change the config items accordingly in ``config_local.ini``.

Set up Database
----------------
Create table customers in Postgresql using the following script::

  create table customers
  (
    id uuid constraint customers_pk primary key,
    first_name varchar(120) not null,
    last_name varchar(120),
    address text,
    post_code varchar(6),
    date timestamp default now()
  );
  create index customers_idx_first_name on customers (first_name);
  create index customers_idx_last_name on customers (last_name);

Change Kafka and Postgresql configurations
------------------------------------------
Copy ``config.ini`` to a new file named ``config_local.ini``, and change the configurations according to your own environment.

How to start
------------
Step 1: If you are using MacOS, make sure file ``bin/i-run`` is executable. You can using the following command::

  Only MacOS need this step, run:
  bash> chmod +x /bin/i-run

Step 2: open a terminal on your computer and start the Kafak producer::

  On MacOS, run:
  bash> ./bin/i-run start producer

  On Windows, run:
  aiven_demo> bin\i-run.bat start producer

You would see the output similar to::

  starting producer...
  producer begins
  [2020.10.24 13:38:04]Sent: {"customer_id": "f1318a36-15a1-11eb-b92c-b46bfc356e10", "first_name": "Leah", "last_name": "Duncan", "address": "1264 Thomas Wells\nCampbellberg, TX 97337", "post_code": "2077"}
  [2020.10.24 13:38:06]Sent: {"customer_id": "f2652b89-15a1-11eb-8fa0-b46bfc356e10", "first_name": "Richard", "last_name": "Rodriguez", "address": "26321 Eugene Trace Apt. 446\nJessicachester, MS 09441", "post_code": "2077"}
  [2020.10.24 13:38:08]Sent: {"customer_id": "f3975385-15a1-11eb-9d3b-b46bfc356e10", "first_name": "Bruce", "last_name": "Davis", "address": "395 Benton Haven Suite 895\nNew Sylvia, KS 85410", "post_code": "2077"}

The above output means messages have been sent to Kafka successfully.

Step 3: open another terminal to start the Kafka consumer::

  On MacOS, run:
  bash> ./bin/i-run start consumer

  On Windows, run:
  aiven_demo> bin\i-run.bat start consumer

You would see the following output::

  Kafka consumer begins...
  [2020.10.24 13:41:03]Received: b'{"customer_id": "17825156-1410-11eb-a4bd-b46bfc356e10", "first_name": "Amber", "last_name": "Cannon", "address": "68002 Brian Grove Apt. 189\\nHebertchester, KS 22409", "post_code": "2077"}'
  [2020.10.24 13:41:03]DB Inserted: insert into customers(id, first_name, last_name, address, post_code) values('17825156-1410-11eb-a4bd-b46bfc356e10','Amber','Cannon','68002 Brian Grove Apt. 189
  Hebertchester, KS 22409','2077')
  [2020.10.24 13:41:03]Received: b'{"customer_id": "18b46261-1410-11eb-9c82-b46bfc356e10", "first_name": "Kaitlin", "last_name": "Hayes", "address": "288 Lisa Stream\\nPort Abigail, OK 10798", "post_code": "2077"}'
  [2020.10.24 13:41:04]DB Inserted: insert into customers(id, first_name, last_name, address, post_code) values('18b46261-1410-11eb-9c82-b46bfc356e10','Kaitlin','Hayes','288 Lisa Stream
  Port Abigail, OK 10798','2077')

From the above output, you can see that the Kafka consumer has been receiving messages and saving them to the database.
