## tictactoe

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

