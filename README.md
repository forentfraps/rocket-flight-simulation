# rocket-flight-simulation
Made a graphical demonstration for rocket flying, considering non-constant mass and air friction, turned out to look pretty cool

*** Theory ***

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

# Im using this input to plot my data manually plot_me("red", a =math.pi/4 , b = math.pi/2.38,fcons =700,fsp = 23000 , v =10)

it is a very horizontal trajectory, much like a real rocket

x1[t]

![image](https://user-images.githubusercontent.com/29946764/159794622-5e3ff90f-abbd-47d4-ab7b-04604f6426ac.png)

v1x[t]

![image](https://user-images.githubusercontent.com/29946764/159794643-bc681ee0-d33f-4c6f-8bb6-1f7b62d77fed.png)

x2[t] 

![image](https://user-images.githubusercontent.com/29946764/159795036-11b726c7-1013-4922-964d-61236d580939.png)

v2x[t]

![image](https://user-images.githubusercontent.com/29946764/159795114-78751a53-fe6c-459f-8bb4-3de2fadc9a6f.png)


z1[t]

![image](https://user-images.githubusercontent.com/29946764/159795316-5335928c-5ed7-4cb9-85f8-4670d94d3754.png)

vz1[t]

![image](https://user-images.githubusercontent.com/29946764/159795378-edc5ce5c-5030-4817-ab1b-ad808609d8ee.png)

z2[t]

![image](https://user-images.githubusercontent.com/29946764/159795497-aed208c9-38bc-4fe8-9b3a-0567b1f49735.png)


vz2[t]

![image](https://user-images.githubusercontent.com/29946764/159795547-b6a28c1f-832c-43b4-a5ea-ed078f1fd79e.png)



Compairing theory and my data, it seems as it is quite similar, which concludes as a success

I will include some actual plots, which my code can perform:

![image](https://user-images.githubusercontent.com/29946764/159795999-c855bf89-531d-428a-8620-2f01a1fa7ff9.png)

![image](https://user-images.githubusercontent.com/29946764/159796041-72b2fb05-cb51-4af1-b0d1-dcd5133473e4.png)

![image](https://user-images.githubusercontent.com/29946764/159796063-31bc7175-3edc-4dc2-b634-178dc3d18a64.png)



**Note:** after a closer look at the code, you could see that wind is indeed in the equation, HOWEVER, it shows wierd results, so it is better left at 0

![image](https://user-images.githubusercontent.com/29946764/159796282-fdc13cd5-4328-49d1-90fe-07a695a201ad.png)

![image](https://user-images.githubusercontent.com/29946764/159796292-3384fd79-4953-4b55-a57d-be8547a3969d.png)


HUGE THANKS TO Chelovechecheggg#5451 for helping
