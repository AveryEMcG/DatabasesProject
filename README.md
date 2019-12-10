# Database Project

Database project is a project implemented in python to
support basic database and table manipulation by an end
user over a text prompt.

## Installation

The python version required for executing the project is 3.6.1
and it runs with intuitive display messages before Input/Output
operations. The entry point for the project is `Project.py` file.
And the flow of execution follows the sequence of steps
afterwards.
The python version required for executing this project is 3.6.1. it runs via an intuitive display messages before Input/Output
operations.

## Operation

The program executes via a series of steps, each of which is prompted to the user.
First - information about the tables is provided - such as number of tables to be added and their names
Second - information about the attributes and FD are entered
Third - addition and deletion of tuples occurs until the user terminates the program

## Misc

This program will run into issues with crashing on python 2.7,
to avoid these problems, be mindful that on python 3.6.1,
user input must be via the format input() and in 2.7 via 
input(). If requiring support on a different version,
this may need to be modified.

