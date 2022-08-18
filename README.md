# image-uploader
To run server, you'll need python3.

For Windows 
- First cd into root directory
- run command `py -3 -m venv venv`
- run command `venv\Scripts\activate`
- run command `pip install flask`
- run command `flask --app main run`

For macOS/Linux 
- First cd into root directory
- run command `python3 -m venv venv`
- run command `. venv/bin/activate`
- run command `pip install flask`
- run command `flask --app main run`

## Questions
### Handling average daily call count 5
We can implement a maximum size for images. If we set this limit to say 8MB, and assume that all images will be
8MB, that is around 40MB per day. If we have 1TB of storage, we will roughly be able to store 120,000 images, which
is around 24,000 days of runway. If we ever run out of storage, we can vertically scale our server by increasing it's memory.

### Handling average daily call count 5,000
That is around 208 calls per hour. We'd be storing a maximum of 40,000MB worth of images per day. If we have 1TB of storage, we'd last
for 25 days max. We can introduce an image compression algorithm for larger images. This would save space for our server.

We can also setup a CDN to serve the static images through the CDN. 

### Handling average daily call count 100,000
4167 calls per hour. We would need to horizontally our servers by increasing the number of machines. And since
each machine would store different images, we partition the data using modulo(counter, N), where counter is the total number
of images, and N is the total number of machines. Also adding a load balancer to evenly distribute the work amongst the servers.
