.. TaskScheduler documentation master file, created by
   sphinx-quickstart on Wed Oct 27 22:42:44 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to TaskScheduler's documentation!
=========================================

This project showcase a simple use case of scheduling algorithms. Scheduling algorithms are held in much regard for designing and implementing Operating Systems [#a]_.
Our project focused on the case of managing task with labelled priorities. The design space of Scheduling algorithms may be categorized into two parts: pre-emptive and non-preemptive algorithms [#b]_.
In the situation that we focused on, task scheduling naturally lend itself to a non-preemptive case because we are concerned to manage a recommendation of task that is to be executed by a human.
That said, we implemented two non-preemptive scheduling algorithms defined in the `Scheduling` class namely: Fist-In First-Out and Shortest Job First. 

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Scheduler Module
----------------
.. automodule:: Scheduler
   :members:
   :undoc-members:
   :show-inheritance:


App Module
----------
.. automodule:: App
   :members:
   :undoc-members:
   :show-inheritance:

References and Indices
======================
.. [#a] Stallings, William (2004). Operating Systems Internals and Design Principles (fourth ed.). Prentice Hall. ISBN 0-13-031999-6.
.. [#b] Silberschatz, A., Galvin, P. B., & Gagne, G. (2013). Operating system concepts essentials. Wiley Publishing.

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
