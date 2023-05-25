# mqtt-python
Python app that resembles a chat space, using MQTT protocol. There is also a Dockerfile for the app.

In the bow-chat.py file set the topic to whatever y want.
Be carefull and do not put the same client_id with others.

To build the image of the docker run the following command in a terminal opened in the folder y have the files that y downloaded,
  docker build -t bow-chat .
To run the container run the following command
  docker run -i -t --name chat bow-chat
  
To test if the app is working run two diffetent containers using the same image, in our case the bow chat image.
For example:
  docker run -i -t --name chat1 bow-chat
  docker run -i -t --name chat2 bow-chat
Write messages and check if it is working properly.
