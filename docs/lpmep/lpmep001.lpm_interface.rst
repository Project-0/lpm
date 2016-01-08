Interacting with LPM
====================

Use Cases
---------

UC001 - Creating a new Project
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

A user wants to create a new project.  In order to do this, he/she must be logged in or have some kind
of access to execute the instruction (see TD001).

Design Decisions
----------------

ED001 - Implement MVC
$$$$$$$$$$$$$$$$$$$$$

The LPM package should be built so that, as a stand-alone application it can serve to create new project
spaces for the user, but can also be provided as a Python package to bundle its operations and
capabilities under other conditions (we should be able to replace the GUI, re-route any controller logic
and leave the rest of the actual business logic untouched).


TD001 - CLI Implementation
$$$$$$$$$$$$$$$$$$$$$$$$$$

In the context of UC001, in order to postpone the provision of a GUI, we have decided to implement the
initial interface for ``lpm`` on the command line with the understanding that a browser-based interface
will be provided in a future iteration.  This method allows users to execute ``lpm`` operations against
their local machine without reliance on Gnome/KDE/Windows/etc.  This implementation is done with the
Python `argparse` library.

Requirements
------------

FR001 - Provide a Functional interface to package operations 
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

Given the decision in TD001 and the accepted expectation of a browser-based GUI, we want to build the
module logic so that it can exist without the CLI GUI.  This means developing code such that a Python
package could be imported into another project, and LPM operations could be performed programmatically
by any of a number of user interface choices.  As ED001 describes, models should be severable from
the rest of an application and non-object system logic should be represented using a Functional
Programming paradigm to fascilitate that.


