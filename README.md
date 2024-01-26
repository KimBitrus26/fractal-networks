
## Fractal Networks

### Prequisites:
`
install docker
install docker-compose
virtual environment,
python3

`

### Preparing your project

- Create a Folder on your Local machine / Computer
- Open Command prompt(git bash) / Terminal in the same folder location

### Cloning the Repository

Visit the project Repository on Github Website: 

- Click on the "Code" button on the Repo page

- Copy the URL  

- In your Terminal, run: git clone repo-url-here

### Creating a virtual environment (for gitbash users)

- run: python -m venv venv (Note i assemed you virtualenv installed.  venv is the name of your virtual environment in this case)
- run: source env/scripts/activate (To activate the virtual environment) or .venv/bin/activate

create an environment variable file .env in the root directory and paste below:

- DJANGO_SECRET_KEY=eahc9fal9n5%!s9h-k%@5ecz=j@5ikxhnokd2e8n21^\)I\)^fnzBGFE

- DEBUG=TRUE
- USE_S3=TRUEno
- USE_LOCAL_DB=TRUEno
- POSTGRES_DB=postgres
- POSTGRES_USER=postgresuser
- POSTGRES_PASSWORD=supersecretevaluation
- DB_HOST=db
- DB_PORT=5432


### Installing Django and other dependencies

- run: pip install -r requirements.txt

### Running the server
I assumed you have docker and docker-compose installed

To build the image and run the containers

- run: sudo docker-compose up -d --build


### Running unit test
To access container's IDs
- run: docker ps

- sudo docker exec -it 'container-id-here' python3 manage.py test

if everything went fine, 1 test will run ok testing postgis model with a pointfield