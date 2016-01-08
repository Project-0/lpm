Putting LPM in a daemon/listener Mode
=====================================

Rationale
---------

LPM is intended to be a project management platform, meaning that it should do more than just create
new projects from templates, get them set up and never be used again.  Many of the features planned
for LPM will, likely, be difficult to use on a command-line, so I want a way to run a listener that can
accept RESTful statements as commands to perform its various functions.

Use Case
--------

UC002 - Interact with LPM system residing on another network location
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

A user wants to create a new project on a remote system.  They should be able to do that without having
to SSH into that system and run this on a CLI.  Development of another interface is a seperate
enhancement, but we should be able to accept these commands from remote clients as well (like browsers,
client-side desktop applications, or other-software-initiated ``curl`` operations.

