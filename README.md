# Airbnb clone - The console
![Screenshot](https://github.com/muhammd2refaat/AirBnB_clone/blob/master/image/65f4a1dd9c51265f49d0.png)

This repository provides the backend for the AirBnB clone project, interfacing it with a console application using the cmd module in Python. The console allows for the user to interact with the system in a more human-friendly way.

## Steps
You won’t build this application all at once, but step by step.

Each step will link to a concept:

### The console

. create your data model
. manage (create, update, destroy, etc) objects via a  console / command interpreter
. store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine
![console](https://github.com/muhammd2refaat/AirBnB_clone/blob/master/image/815046647d23428a14ca.png)