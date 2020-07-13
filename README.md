# Zoom Waiting Room Queue

## Description:
This project implements a queue feature for Zoom's waiting room feature using image grabing and image-to-text processing. Specify to the program where the waiting room will be located and the program will work on that specific area when running.

## Commands:
When using the program, it takes certain keywords that perform different functions for the user to use. The specifc keywords and their functions are listed in the table below.

| Command | Function Description                                                                                                           |
|---------|--------------------------------------------------------------------------------------------------------------------------------|
| NEXT    | Produces the next entity in the queue while also removing it from the queue.                                                    |
| CHECK   | Tells the program to screenshot the current waiting room and update the queue with any new entities if it sees any.               |
| EMPTY   | Empties the queue.                                                                                                             |
| PRINT   | Prints all entities inside of the queue.                                                                                       |
| QUIT    | Ends the program.                                                                                                              |
| DEBUG   | Enables debugging. When issuing the "CHECK" command, the user will now see a picture of where the program is taking a picture. |
| HOST    | Displays the name of the host of the Zoom call.                                                                                |
