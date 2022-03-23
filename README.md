# rocket-flight-simulation
Made a graphical demonstration for rocket flying, considering non-constant mass and air friction, turned out to look pretty cool

For such tasks involving non-constant mass I will be using the *mesherskiy equation*

![image](https://user-images.githubusercontent.com/29946764/159786382-89347625-0936-4b18-a36b-2535b704c116.png)


"F.." means external forces, such as air friction and gravitation pull

![image](https://user-images.githubusercontent.com/29946764/159786537-a4ddaf49-6d77-4fe7-829b-653450884776.png)


Our rocket will have 2 phases:
    - With fuel, meaning differing mass, drag from the fuel exhaustion
    - Without fuel, constant mass, basically only air friction

![image](https://user-images.githubusercontent.com/29946764/159786945-517c5ee2-cec4-41fe-ad94-85619401a853.png)

After all those preparations we can finally make out final equations 

![image](https://user-images.githubusercontent.com/29946764/159787344-d4862e19-aa21-4866-9273-aad2ae614628.png)

After expanding it into a 3 equation system it turnes out to be non-linear differential equations, which i am not going to solve analytically
However we can try them out with some test data, to later reffer to this as an expected result 
*Note:* I will be doing x/y reffering to horizontal/vertical plane, however in the code x\y is horizontal and z in vertical
**PART 1**

![image](https://user-images.githubusercontent.com/29946764/159787772-13656a7d-63ef-4c58-8041-154328aa14b2.png)

**PART 2**

![image](https://user-images.githubusercontent.com/29946764/159787825-f77bca53-4a7e-40ee-b223-f7a30b3927e2.png)

***Testing Theory***
x1[t]

![image](https://user-images.githubusercontent.com/29946764/159794622-5e3ff90f-abbd-47d4-ab7b-04604f6426ac.png)

v1x[t]

![image](https://user-images.githubusercontent.com/29946764/159794643-bc681ee0-d33f-4c6f-8bb6-1f7b62d77fed.png)


HUGE THANKS TO Chelovechecheggg#5451
