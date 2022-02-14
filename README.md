# Purpose of this Sandbox
This is sandbox running a simple Python Application with Docker and Falcon framework. You can use this to troublshoot Falcon and/or Docker APM configuration issues.

# Requirements: 
Need to have Docker Installed on the machine. 

# Python Falcon APM Sandbox
This is a sample falcon 'hello world' app with APM configurations in a docker-compose file.

### Create a custom .env file

Make sure that in your ~ directory, you have a file called sandbox.docker.env that contains:

```
DD_API_KEY=<Your API Key>
```

# STEPS:
1. Run `docker-compose build` to build the docker image
2. Run `docker-compose up` to spin up the containers
3. On another terminal run: docker exec -it falcon_app bash
4. Curl localhost:8000/falcon_app a couple of times to generate traces (should get 'hello world' response) 
8. See traces in your account


Remember to run `docker-compose down` to stop and remove the containers
