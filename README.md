# Test_Innovamat

As a part of the MVP of the Innovamat application, it is needed to develop a functionality to provide the students a set of activities of an area (for example calculus) so they can do the learning process correctly.

The activities are grouped in itineraries and each activity has a difficulty. The difficulty (D) is a natural number between 1 and 10. An itinerary may include multiple activities with the same difficulty. There is an absolute order (0) in each itinerary. The order satisfies that if two activities have difficulties Di and Dj respectively with Di < Dj, then Oi < Oj, where O is the position of the activity in the order. There cannot be repeated activities in the same itinerary.

The activities are characterized by their name and an identifier. An activity can include several exercises. To evaluate the result, the activities also have the solution of every exercise and an estimation of the total time that should be spent to complete it.

The application works in the following way: (Assuming that there is a set of activities in the itinerary, with at least one activity for each level of difficulty.)

The student asks for an activity to the API.

If the student has not started the itinerary, the API will return the first activity in the itinerary.
If the student has completed the itinerary, that is to say, the student has solved the last activity of the itinerary correctly, the API will return a response saying that there are no more available activities, since the itinerary has already been completed.
Once the student gets the next activity to do, he/she will do all the required exercises through the application. When done, the application will send the results to the API, specifying the following parameters:

The identifier of the activity obtained in the previous step.
The identifier of the student who has solved the activity.
A string with the ordered results of the exercises done. For example, for an activity with 4 exercises: "1_34_-5_'none'".
The time spent by the student to do the activity.
When the API recieves the request to complete the activity, it will process it and it will return the proper result to indicate if it has been registered correctly or not. To consider that an activity is correctly completed, it is necessary to give an answer for every exercise in the activity.

When an activity is completed, the API will process which is the next activity that should be returned to the student when he/she asks for the next activity. 
