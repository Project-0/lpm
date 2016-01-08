LPM Module Design
=================

The modularity of LPM's sub processes is driven, in no small part, by ED001 regarding the assumption
that all software built in an Agile environment will need to be extended.  Since we don't know what
kind of things users of LPM will want the engine to be able to do, we can, at least, design for growth.

In that spirit, we want the core portion of LPM to act as a very programmable controller.  These
modules are one kind of model in that pattern.  Given that, LPM modules should provide an easily
extensible mechanism to allow the LPM engine to execute commands to the sub-system being accessed.

ED001
-----

My inclination is to pilot that process on the git module as that one is a more imminent need.  That
being the case, we will start with an object model, a number of functional-style views, unit tests
and a front-end-specific GUI module.

Requirements
------------

FR001 - Deliver a module, consumable by LPM, that implements git functionality
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

So, we are looking at, probably wrapping the existing ``py-git.Repo`` object, and adding a few
functional operations to a ``views.py`` file.  Then we would need a way to inject the git module into
config and CLI arg parsing operations as needed.
