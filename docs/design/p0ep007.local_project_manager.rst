Design Rationale
================

Everything about this project is focused on creating a software tool so that new projects can be created and collaborated on quickly and easily.

Design Decisions
----------------

The following decisions have been made at different levels regarding this feature.  They are marked with their motivating requirement(s) and accompanied by use cases.

Executive Decisions
```````````````````

ED001
$$$$$

**Templating**
In the context of UC001, facing the problem with defining exactly what a project *is*, we decided that ``lpm`` will support a project templating model implemented such that users can define a template or import templates defined by other users, so that the software is capable of supporting a variety of project types (static web sites would require a different setup, perhaps, than a Linux kernel module, for instance).  We recognize that this forces the complexity of our problem's solution into the template framework, but it also allows each template's author to define what that project consists of on a case-by-case basis.

ED002
$$$$$

**Modularity**
Given the context of UC001, and the need to kickoff bootstrapping or boilerplate/setup processes, we have decided that ``lpm`` will support an ability to execute operations found in external software systems.  This will allow ``lpm`` to handle bootstrapping those systems, though the need to install configure and, possibly extend those submodules might make this more complex.

Requirements
------------

FR001
$$$$$

**Allow users to create new projects**:  This, understandably, entails knowing what a project needs (see FR002 - Templating), and then doing the boilerplate setup and bootstrapping to get the workspace defined

FR002
$$$$$

**Define a Project Template system**:  The rationale for this is given in ED001, but the template system must support the ability to bootstrap or set up any attached modules (see FR003).

FR003
$$$$$

**Extend the interfaces of external software dependencies and bundle them as modules in ``lpm``**:  See ED002 for rationale.  External systems (like, ``git`` or ``virtualenv``) should be usable to get the project started.

Use Cases
---------

UC001
$$$$$

**Start New Project**:  User has an idea for a software project he wants to build and uses ``lpm`` to create the project space [FR001].  Deciding that he will need to create a directory structure for a basic (language and/or platform agnostic) project [FR002], and then create a VC repository for the necessary artifacts (soure code, documentation, license and readme info, etc.)
