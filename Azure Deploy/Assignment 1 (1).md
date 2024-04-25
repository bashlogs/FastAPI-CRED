**Assignment – 1**

**API Development and Cloud Infrastructure**

Problem Statement - Design and implement 4 simple CRUD APIs using Python FastAPI, integrating it with a PostgreSQL database. Deploy the API on Azure cloud infrastructure and provide step-by-step documentation of the deployment process. Also, ensure the API is secure and scalable.

1)  Go to my github profile and clone the code - <https://github.com/bashlogs/FastAPI-CRED.git>

2)  Create a PostgreSQL Server

3)  Build a container registery and deploy the application

**Create a PostgreSQL Server**

![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.001.png)

Go to Azure database for PostgreSQL servers

![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.002.png)

Click on create and fill the information’s and choose the workload type depending upon your use

I am using free tier development workload.

![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.003.png)

Select authentication method for PostgreSQL Login

![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.004.png)

Give Access to all IP address




![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.005.png)

Check the details once again and create the server

![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.006.png)

We can add this firewall later so continue server without firewall rules





![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.007.png)

Wait for few minutes to complete deployment process

![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.008.png)

Once the server is deployed go the networking and give public access to the current client IP address

![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.009.png)

After this go to the databases -> Click on Add -> Create a database “python\_db”

Once the database is created click on connect option azure shell will pop up

![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.010.png)

In that azure shell you will see the username, host,  port and dbname note down that information

**Now let’s connect azure database to our local pgadmin4**

![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.011.png)

Go to server menu and click on register new server and enter host name

For ex:-  HostName = “john.postgres.database.azure.com” Then name =  john

![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.012.png)

The go to connection tab and enter hostname, port, database and username with password

Click on save and your server will be register

![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.013.png)

Server register successfully

![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.014.png)

If you go to table their will be no table now run the fastapi application with given readme instructions.









![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.015.png)

Execute a create query.

![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.016.jpeg)

Refresh the table you will see entry of create query.





**Deploy the application in container registry**

![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.017.png)

Go to container registry and enter the registry name

![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.018.png)

![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.019.png)

Skip the networking and encryption tabs

![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.020.png)

Check the details and create the container

![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.021.png)

Container is successfully created


![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.022.png)

Once the container created go to the Access key tab and enable admin access

Next step is to go terminal and do docker login

Commands : 

docker login <login\_server> -u <username> -p <password>

docker build -t mayurkhadde.azurecr.io/fastapi:1.0 .

![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.023.png)

Application successfully deployed

![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.024.png)

Go to the repositories and see if the application deployed






**

**Create a container instance**

![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.025.png)

Go to the container instance and create instance

![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.026.png)

Enter same repository name to the container name and select image source as azure container registry

![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.027.png)

FastAPI Application runs on the 8000 port so enter that port number in networking

![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.028.png)

Enter your environment variables in advanced tab


![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.029.png)

Review the things and create the instance

![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.030.png)

Container instance is created successfully




![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.031.png)

If you don’t see any red or orange label then your instance is running fine

Select the public IP address and check if the API is running or not

![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.032.png)

Application is running






![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.033.png)

Try to execute select query

![](Aspose.Words.aeab3f02-ef92-40ca-841b-3c917b014e0f.034.png)

Once you perform all this step you application will be running perfectly fine




