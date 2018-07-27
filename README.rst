=====
kmonitor
=====

This is a docker setup for a plugable monitoring service

Note that kmonitor is under development and not yet feature complete.

The latest source code is available at http://github.com/kartoza/kartoza-monitoring.

* **Developers:** See our `developer guide`_


Project Activity
--------------

|ready| |inprogress|

|throughput_graph|

* Current test status master: |test_status_master| 

* Current test status develop: |test_status_develop| 


Quick Installation Guide
------------------------
For deployment we use `docker`_ so you need to have docker
running on the host. kartoza-monitoring is a django app so it will help if you have
some knowledge of running a django site.



    git clone git://github.com/kartoza/kartoza-monitoring.git

    # to build the django docker environment run the following commands

    make build

    make permissions

    make web

    # Wait a few seconds for the DB to start before to do the next command

    make migrate

    # to then build the monitoring stack run

    make monitoring

U can then access grafana on URL: 0.0.0.0:3000

Install as a Django Package
---------------------------

1. Add "kmonitor" to your INSTALLED_APPS setting like this:

    INSTALLED_APPS = [
        'kmonitor',
    ]

Thank you
_________

Thank you to the individual contributors who have helped to build kartoza-monitoring:

* Alison Mukoma: alison@kartoza.com

