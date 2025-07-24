Version 1.0
==============================================

Version 1.0 is the latest version of JMEF. It was realesed on June 2nd, 2025.

Documentation
-------------

Visit the :doc:`doc` page to see all allowed tags and attributes


Examples
--------

Below you can find a few examples demonstrating JMEF usage:

- Full JMEF example using all of the allowed tags and attributes: `jmef.xml <jmef.xml>`_
- Minimal valid JMEF example using only required tags and attributes: `jmef_minimal.xml <jmef_minimal.xml>`_

Schema
------

Journal Metadata Exchange Format schema for version 1.0 is available here: `jmef.xsd <jmef.xsd>`_

To use it just include it in your XML document:

.. code-block::

   <journal xmlns="https://jmef.icm.edu.pl/version-1.0" xsi:schemaLocation="https://jmef.icm.edu.pl/version-1.0 https://jmef.icm.edu.pl/version-1.0/jmef.xsd">
       ...
   </journal>

