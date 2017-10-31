# CarPooling-Server
The server part of mobile final project.
## APIs offered by server
### Get
1.listAllCarPools(Query query)    return List<CarPools>		<br>
2.getHistory(User)    return List<CarPool>
  
### Post
1.makeReservation(CarPool, User)    return CarPool  <br>
2.makeOffer(CarPool)    return CarPool    <br>
3.getCarPools(Query query)    return List<CarPools>   <br>
4.registered(User user)   <br>
5.login(User user)   

### Put
1.updateSettings(User user)
  
### Delete
1.cancelReservation(CarPool, User)

## Object



