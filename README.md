
# Chatting Application




## Role of the Server
Server is receiving all the events from the client and performing the following	action
 - Broadcasting the message
 - sending message to specific client 
 - dealing with the mathematical expression.
## Threads at server side:
    Whenever a new client is added to the server,  a new thread is created.  
    This particular thread deals with that respective client.  
##### As shown in the image:  
    3 users are connected to the server , means 3 threads are running at the server, their id is displayed, along with their name.
![server](https://lh3.googleusercontent.com/pw/AP1GczOlmnwgrdK2ctVt5EuELj8njLVZHNGwWRYI8xdxSTX0ury8-WueSzlHMz_n3xA3DjG6ZmnSG7oHNff-ICchfWIo7KLIHQKQ9jmBmJDvFhyIvhLCA6eG3g-YmSfc4YLTqJguaCkE-SMSThj8Gst6kNUw=w963-h513-s-no-gm?authuser=1)

## Role of client
    As shown 3 clients are connected.  
    At each client ,four functions are given.  
#### Send: 
    it is used for broadcasting the message to all the connected clients.  
#### Calculate:  
    It is used for calculating some mathematical expressions.  
    Here, expressions is written at the client side and calculation  is done at the server side and the result is sent back to the particular client.  
#### Specific user:  
    Instead of broadcasting, if a user wants to chat with a particular user,        then this function will be used.   
    To send the message to specific user need to specify their name along with the message.  
#### Know all users: 
    using this a particular client can know all the connected users.

#### Other functionality:
		When a new user is connected to the server, then a broadcast will happen from  the server telling the name of the new user to the clients.
#### Thread at client side:
		At each client two thread are running,
		First thread is displaying all the messages and dealing with GUI.  
		Second thread is used for receiving the message.

#### Client picture 1: 
    This picture showing when all clients are just connected to the server.
![picture1](https://lh3.googleusercontent.com/pw/AP1GczOb9UN9yTaU8L-dxgNl16BOIRU2gAMnGcd78RjjclE3O8QdUWx0oY5NjFhC-S9XRKox87idzrQPJ1IZqyspKHnpa4hyJ-7t45-DPjeufQn3QQoYDQ6nJ2F-swAmmJLhOnsKViyEhm9rO6CEXwhkXSgw=w1094-h615-s-no-gm?authuser=1)

#### Client Picture 2: 
    nitesh is using the send button to broadcast the message.

![picture2](https://lh3.googleusercontent.com/pw/AP1GczPWfnKE-K-x32aC9ip10PGF_5J8yCn5XxgfEuOGucp_Y9nrIApadix1gVm_2ZTC36i0nQd7OItGdcohCUGbXem6FL3IlXbwthSaAezrtbBUhpm5mvXNaz9M8i67MwY1c3OLlmOvB2jkxv3lnxL4Gf2c=w1094-h615-s-no-gm?authuser=1)

#### Client picture 3:
    Hariom has used the calculate function to calculate some expressions and it’s result is display to only hariom.

![picture3](https://lh3.googleusercontent.com/pw/AP1GczPLnkNP-LFuzmr9vnMEDm5IObFJvP8W1F8n8_NEIW-9hWvpUWhRoeDOXS_Mt3hylig8JemxdP3Ri-EV9-_NiuZefVZQiLm7oQunyDsz24pMwuY2aWu2pOThwiFO0GyFIHVG9KDIqwCUFcnfs22Syqmu=w1094-h615-s-no-gm?authuser=1)


#### Client picture 4:
    Hariom is sending message to only rajat using specific user function.
![picture 5](https://lh3.googleusercontent.com/pw/AP1GczNLiA16CHW5Ifo93A1c6taP9TxzYX_G54JuLu_i2tjaMukyL70btJ4eOjionFNU_TW29ZpQcYTMO9dPYsdgFl-0X8pBcOTos0Ktzj2Njr_JJzKEtgCZ_ePi6ZDbr6xYJr1BPlL-wvIsXjPBqtIpaEyF=w1094-h615-s-no-gm?authuser=1)

#### Client picture 5:
    Hariom has used know all user function to list the all the user connected.
![picture 5](https://lh3.googleusercontent.com/pw/AP1GczPKUQaq0uDVTNWnsFRhDfw-7Isx0f9r94DYHRktQIYQet8DJApYbfQRmG9YVE8SZwodUvxe3FsRLjCycgkZ7fi5DucboXG5tiTUdYsCNTnUDCWznoAQWaDkBho-daRtSNgz63FSZ44H5_-rye2Q4_aD=w1094-h615-s-no-gm?authuser=1)


## Authors

- [@Nitesh](https://www.linkedin.com/in/nitesh-yadav-b8847616b/)


## Deployment

To deploy this project run  
###### First start the server
```bash
  python3 server.py
```
then start the required number of clients

```bash
 python3 client.py
```

## Feedback

If you have any feedback, please reach out to us at     cs23m110@iittp.ac.in   
or niteshyadavand2000nitesh@gmail.com
    

