# Owl's Project Template

A package for developing, building and deploying machine learning API services
as docker containers using my current workflow.

## Structure

Template is based around the following workflow:

- Define extraction steps e.g. SQL or pandas code in `src/extract/`
- Sample data goes into `data/`
- Develop ideas in jupyter `notebooks/`
- Refactor methods to `src/`, add tests to `test/`, replicate notebook results
- Write train and predict jobs into `src/`
- Build any deployment binaries in `bin/` e.g. TF models
- Serve model over flask api from `web/`
- Retrain model from `web/`, store models in `bin/`

Makefile offers the following calls

- **build** - Build the docker container for serving / deployment
- **note** - Run a jupyter notebook server on localhost:8888
- **test** - Run unit tests and linter
- **serve** - Run a local web server for endpoint testing (e.g. with Postman)

We explicitly dont cover how to actually host / serve a model - kubernetes is a solid
choice, but I've had this setup working on ECS and Heroku as well.


## Local setup

The project uses Docker to run everything locally so you'll need to install and run
the docker client from https://docs.docker.com/docker-for-mac/install/ (assuming
you're a mac user).

Clone the repo, then copy and paste  `./credentials.env.examples` 
to `./credentials.env` and update the environment credentials.

Then run `make build` from the root directory to build the containerss.

To launch a notebook server for local work, run `make note`. The `src/`, `data/`,
`notebooks/`, `web/` and `bin/` directories will all be mounted locally at `/app/`.


## Running on Kubernetes

To run on kubernetes locally we'll need to install:
- Kubectl - A command line app for interacting with kubernete
- VirtualBox - A VM host to run a local kubernetes cluster
- Minikube - A command line app for installing and running a local kubernetes
cluster inside of VirtualBox
- Kompose - A command line tool for launching our docker-compose.yaml file
as a kubernetes service

Manually install VirtualBox (yuk!) from here first:
https://www.virtualbox.org/wiki/Downloads

Then install the command line apps:

```
brew install kubernetes-cli
brew cask install minikube
brew install kompose
```

You may need a free account on Docker Hub ... you can get it here:
https://hub.docker.com/

If running on Mac you'll need to change a setting in your local docker install. Open
Docker > Preferences, untick the "Securely store Docker logins in macOS keychain"
then restart docker. This is because Kompose does not support macOS keychain yet!

Now we're ready to rock.

```
# Start the local kubernetes cluster
minikube start

# See what services as running (should be none)
kubectl get pods

# Launch the dashboard
minikube dashboard

# Build and launch our services
kompose up

# Open our Jupyter web service - this should open a browser to the login page
minikube service dev

# List the post again to get the service hash
kubectl get pods

# Tail the jupyter service logs to get the login token - replace the token with
#  whatever it's called on your machine (from last step)
kubectl --namespace default logs dev-69498c9986-b8n5x
```

You should now be able to log into the jupyter service running on Kubernetes!

To bring it back down again do:

```
# Stop and delete the services we launched
kompose down

# Spin down the minikube cluster
minikube stop

# OPTIONAL - Delete the local minikube VM
minikube delete
```
