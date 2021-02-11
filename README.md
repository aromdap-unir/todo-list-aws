# todo-list-aws

### The application: A simple Python to-do-list

The app has a series of funcions that will interact with the user through an API. In this case, since we are working on an AWS context, an API Gateway.

The following are the functions that this app will have:
- Create
- List
- Get
- Update
- Translate 
- Delete

The function translate is based on the Comprehend and Tranlate natural language processing frameworks.

You can get to know more about these AWS technologies [here](https://docs.aws.amazon.com/translate/latest/dg/what-is.html).



## Introduction: Serverless Framework

This project aims at deploying a Pyhton app in its function-based structure in a Serverless Framework . Since the cloud provided is AWS, the template.yaml will have to declare in conjunction with our provided.

Before doing so, we recommend to go through the [Serverless Framework documentation](https://www.serverless.com/framework/docs/providers/aws/)


![alt text](https://www.google.com/imgres?imgurl=https%3A%2F%2Fres.cloudinary.com%2Fpracticaldev%2Fimage%2Ffetch%2Fs--J1M-pSXo--%2Fc_imagga_scale%2Cf_auto%2Cfl_progressive%2Ch_420%2Cq_auto%2Cw_1000%2Fhttps%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F1qg3vu3nsm7krae8qk4s.png&imgrefurl=https%3A%2F%2Fdev.to%2Fmquanit%2Fcreate-deploy-your-first-ever-aws-lambda-function-by-serverless-framework-2hga&tbnid=5UXXyKGVIEGyWM&vet=12ahUKEwiO1Yah3OLuAhVJ1uAKHUkZA4EQMygzegQIARAw..i&docid=KfcER-HgS8iGmM&w=1000&h=420&q=serverless%20framework%20aws&client=ubuntu&ved=2ahUKEwiO1Yah3OLuAhVJ1uAKHUkZA4EQMygzegQIARAw)

### Serverless Framework: first steps

Install the serverless CLI:
```
npm install -g serverless
```

Run below command and follow the prompts
```
serverless
```

Once you’ve signed up for Pro, login to your Pro dashboard from the CLI:
```
serverless login
```


### The deployment:

The template.yaml will help to properly deploy the application into an AWS EC2 instance when building a simple pipeline.

In this case, two pipelines should be built in order to cover the staging and the production environments, that will match with the Master and Develop branches of the GitHub repository.

Anytime a pull request is done against any of the branches, it will trigger the automated build and deployment of the app.





The aim of this project was to adapt the existing structure of a simple to-do-list application from its function-based shape to an object oriented approach.

This project is split in different parts:
    1. Build and deploy todo-list app in Serverless Framework via Github repository
    2. Implement new feature in Python to translate any of the inputs stored in DynamoDB
    3. Migrate Github repository to AWS CodeCommit
    4. Migrate app project from Serverless Framework to SAM Framework 
    5. Run SAM locally with DynamoDB instance in a Docker Network
    6. Operate and test manually that all endpoints work as expected
    7. SAM Build & SAM Deploy to AWS
    8. Operate and test manually that all endopoints work as expected


