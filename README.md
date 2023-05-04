## tictactoe [![Docker Image CI](https://github.com/karthikeyanrathore/tictactoe/actions/workflows/docker-image.yml/badge.svg)](https://github.com/karthikeyanrathore/tictactoe/actions/workflows/docker-image.yml)

![tictactoe](https://github.com/karthikeyanrathore/tictactoe/blob/main//src/assets/demo.gif)

## running application 
```bash
# build docker image
docker build . -t karthikeyan/tictactoe

# run docker container, expose conatainer port to host.
docker run --name tictactoe -d -p 8080:8080 karthikeyan/tictactoe

docker logs -f tictactoe

# stop tictactoe
docker stop tictactoe

# remove service
docker rm tictactoe
```

## How to upload and run from docker-hub?
```bash
# upload image to dockerhub registry (tag + push)
docker tag karthikeyan/tictactoe karthikeyanisusingdocker/tictactoe
docker push karthikeyanisusingdocker/tictactoe

# pull it locally in a new environment + run app
docker pull karthikeyanisusingdocker/tictactoe
docker run karthikeyanisusingdocker/tictactoe
```

