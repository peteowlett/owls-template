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


## Links

Data sets

- https://machinelearningmastery.com/time-series-datasets-for-machine-learning/
- https://archive.ics.uci.edu/ml/datasets.html?format=&task=&att=&area=&numAtt=&numIns=&type=ts&sort=nameUp&view=table

LSTM Approach

- https://www.kaggle.com/niyamatalmass/machine-learning-for-time-series-analysis
- https://blog.statsbot.co/time-series-prediction-using-recurrent-neural-networks-lstms-807fa6ca7f
- https://towardsdatascience.com/using-lstms-to-forecast-time-series-4ab688386b1f

PyMC Approach

- https://docs.pymc.io/notebooks/GLM-poisson-regression.html

