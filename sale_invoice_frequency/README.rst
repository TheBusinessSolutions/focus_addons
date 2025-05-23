======================
Sale Invoice Frequency
======================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:144cf67b24d332a903d14252ffd1ef1fc6c1d0b46e72c2705d100bb2f72de4be
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :target: https://github.com/OCA/sale-workflow/tree/15.0/sale_invoice_frequency
    :alt: OCA/sale-workflow
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/sale-workflow-15-0/sale-workflow-15-0-sale_invoice_frequency
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=15.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module extends the functionality of sales to support group by Invoicing
frequency and to allow you to choose the right orders to invoice based on the
frequency defined on the customer.

**Table of contents**

.. contents::
   :local:

Usage
=====

To use this module, you need to:

#. Go to *Sales/Configuration/Invoicing frequency* and create your custom
   frequencies.
#. Set these frequencies in the customer form *Sales and purchases* tab.
#. When a sale is created, the Invoicing frequency of the field ``partner_id``
   is propagated.
#. An user can change Invoicing frequency on sales and customers if has group
   ``account.group_account_invoice``.
#. You can change Invoicing frequency on a sale on the *Other information* tab
   without changing the customer frequency.
#. When you want to invoice, group sales by Invoicing frequency and invoice it.
#. You can create a CRON for each frequency to automate invoicing action.

Known issues / Roadmap
======================

* Add an automation to auto-invoice orders. Now must be done grouping orders by
  invoicing frequency and invoice them manually.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/sale-workflow/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_invoice_frequency%0Aversion:%2015.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Moduon

Contributors
~~~~~~~~~~~~

* Eduardo de Miguel (`Moduon <https://www.moduon.team/>`__)
* Rafael Blasco (`Moduon <https://www.moduon.team/>`__)

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

.. |maintainer-Shide| image:: https://github.com/Shide.png?size=40px
    :target: https://github.com/Shide
    :alt: Shide
.. |maintainer-yajo| image:: https://github.com/yajo.png?size=40px
    :target: https://github.com/yajo
    :alt: yajo
.. |maintainer-EmilioPascual| image:: https://github.com/EmilioPascual.png?size=40px
    :target: https://github.com/EmilioPascual
    :alt: EmilioPascual

Current `maintainers <https://odoo-community.org/page/maintainer-role>`__:

|maintainer-Shide| |maintainer-yajo| |maintainer-EmilioPascual| 

This module is part of the `OCA/sale-workflow <https://github.com/OCA/sale-workflow/tree/15.0/sale_invoice_frequency>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
