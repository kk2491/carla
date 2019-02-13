Python 3.5.2 (default, Nov 12 2018, 13:43:14) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import carla
>>> exit()
KeyboardInterrupt
>>> 
>>> 
>>> client = carla.Client('localhost', 2000)
>>> 
>>> client.set_timeout(10.0)
>>> 
>>> world = client.get_world()
>>> 
>>> print(world)
World(id=4,map_name=Town03)
>>> 
>>> actors = world.get_actors()
>>> print(actors)
[Actor(id=1, type=spectator), Actor(id=2, type=traffic.traffic_light), Actor(id=3, type=traffic.traffic_light), Actor(id=4, type=traffic.traffic_light), Actor(id=5, type=traffic.traffic_light), Actor(id=6, type=traffic.traffic_light), Actor(id=7, type=traffic.traffic_light), Actor(id=8, type=traffic.traffic_light), Actor(id=9, type=traffic.traffic_light), Actor(id=10, type=traffic.traffic_light), Actor(id=11, type=traffic.traffic_light), Actor(id=12, type=traffic.traffic_light), Actor(id=13, type=traffic.traffic_light), Actor(id=14, type=traffic.traffic_light), Actor(id=15, type=traffic.traffic_light), Actor(id=16, type=traffic.traffic_light), Actor(id=17, type=traffic.traffic_light), Actor(id=18, type=traffic.traffic_light), Actor(id=19, type=traffic.traffic_light), Actor(id=20, type=traffic.traffic_light), Actor(id=21, type=traffic.traffic_light), Actor(id=22, type=traffic.traffic_light), Actor(id=23, type=traffic.traffic_light), Actor(id=24, type=traffic.traffic_light), Actor(id=25, type=traffic.traffic_light), Actor(id=26, type=traffic.traffic_light), Actor(id=27, type=traffic.traffic_light), Actor(id=28, type=traffic.traffic_light), Actor(id=29, type=traffic.traffic_light), Actor(id=30, type=traffic.traffic_light), Actor(id=31, type=traffic.traffic_light), Actor(id=32, type=traffic.traffic_light), Actor(id=33, type=traffic.traffic_light), Actor(id=34, type=traffic.traffic_light), Actor(id=35, type=traffic.traffic_light), Actor(id=36, type=traffic.traffic_light), Actor(id=37, type=traffic.traffic_light), Actor(id=38, type=traffic.traffic_light), Actor(id=39, type=traffic.traffic_light), Actor(id=40, type=traffic.speed_limit.90), Actor(id=41, type=traffic.speed_limit.90), Actor(id=42, type=traffic.speed_limit.60), Actor(id=43, type=traffic.speed_limit.60), Actor(id=44, type=traffic.speed_limit.30), Actor(id=45, type=traffic.speed_limit.30), Actor(id=46, type=vehicle.seat.leon), Actor(id=47, type=sensor.other.collision), Actor(id=48, type=sensor.other.gnss), Actor(id=49, type=sensor.camera.rgb)]
>>> actors = world.get_actors()
KeyboardInterrupt
>>> 
>>> 
>>> for actor in world.get_actors():
...     if actor.attributes.get("role_name") == 'hero':
...             ego = actor
...             break
... 
>>> 
>>> print(ego)
Actor(id=46, type=vehicle.seat.leon)
>>> 
>>> 
>>> 
>>> gnss_sensor = world.get_blueprint_library().find('sensor.other.gnss')
>>> 
>>> print(gnss_sensor)
ActorBlueprint(id=sensor.other.gnss,tags=[gnss, other, sensor])
>>> transform = carla.Transform(carla.Location(x=0.8, z=1.7))
>>> gnss_sensor_attach = world.spawn_actor(gnss_sensor, transform, attach_to=ego)
>>> 
>>> gnss_sensor_attach.listen(lambda data: print(data))
>>> GnssEvent(frame=627448, lat=49.0011, lon=7.99894, alt=1.74741)
GnssEvent(frame=627447, lat=49.0011, lon=7.99894, alt=1.74741)
GnssEvent(frame=627449, lat=49.0011, lon=7.99894, alt=1.74741)
GnssEvent(frame=627450, lat=49.0011, lon=7.99894, alt=1.74741)
GnssEvent(frame=627451, lat=49.0011, lon=7.99894, alt=1.74741)
GnssEvent(frame=627452, lat=49.0011, lon=7.99894, alt=1.74741)
GnssEvent(frame=627453, lat=49.0011, lon=7.99894, alt=1.74741)
GnssEvent(frame=627454, lat=49.0011, lon=7.99894, alt=1.74741)
GnssEvent(frame=627456, lat=49.0011, lon=7.99894, alt=1.74741)
GnssEvent(frame=627455, lat=49.0011, lon=7.99894, alt=1.74741)
GnssEvent(frame=627457, lat=49.0011, lon=7.99894, alt=1.74741)
GnssEvent(frame=627458, lat=49.0011, lon=7.99894, alt=1.74741)
GnssEvent(frame=627459, lat=49.0011, lon=7.99894, alt=1.74741)
