# python-http-server
A simple Python HTTP Server that serves static content
There are several ways that this small application can be run:

### Running as a Systemd Service
- In the [Service File](python-systemd-http-server), change the `User` property to the user that is going to be running the server, the default is jenkins:
	```systemd
	[Service]
	User=jenkins
	```
- Install the server
	```bash
	sudo make install
	```
- Start the Server with `systemctl`
	```bash
	sudo systemctl start python-systemd-http-server
	```
- The server can be accessed on the default port of `9000`:
	```bash
	http://localhost:9000
	```

### Running in a Docker container
- Build the docker image and run the container:
```shell
make docker_up
```

