# rocket-flight-simulation
Made a graphical demonstration for rocket flying, considering non-constant mass and air friction, turned out to look pretty cool

I will be using meshchersky equation to compute my trajectory
![image](https://user-images.githubusercontent.com/29946764/159598462-2eda823c-e62a-445a-b9d8-93e8c4a5fce7.png)
Trying the theory also in wolfram to see what to aim for

1st part :

![image](https://user-images.githubusercontent.com/29946764/159599894-b35580c7-2793-449f-be19-07c926f7b8ba.png)

2nd part:

![image](https://user-images.githubusercontent.com/29946764/159598523-7c831299-a34c-462e-b982-480abe7a24d4.png)

I chose SciPy, however i also tried SymPy, but it seemed to struggle a lot and coulnt solve given equations

When trying my model it seems that resuts are pretty accurate:

![image](https://user-images.githubusercontent.com/29946764/159598702-d0067f92-43a5-43a5-a2f2-a0bd4cf66920.png)

After playing around with fuel consumption and angles i also got these interesting results:

![image](https://user-images.githubusercontent.com/29946764/159598829-7ec59928-e72e-4ad3-91b4-a0a5d56aeb1e.png)

![image](https://user-images.githubusercontent.com/29946764/159598844-0934e345-88bb-4f52-a95d-2ef06e222ad0.png)

Such odd behaviour could be explained by air friction being proportional to speed^2 which slows down substantially but then it speeds back up, due to fuel being left
