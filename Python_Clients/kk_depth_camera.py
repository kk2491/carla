import carla
import time
import scipy.misc
import numpy

def to_bgra_array(image):
	"""Convert a CARLA raw image to a BGRA numpy array."""
	# if not isinstance(image, sensor.Image):
	# 	raise ValueError("Argument must be a carla.sensor.Image")
	array = numpy.frombuffer(image.raw_data, dtype=numpy.dtype("uint8"))
	array = numpy.reshape(array, (image.height, image.width, 4))
	return array

def depth_to_array(image):
    	array = to_bgra_array(image)
    	array = array.astype(numpy.float32)
    	# Apply (R + G * 256 + B * 256 * 256) / (256 * 256 * 256 - 1).
    	normalized_depth = numpy.dot(array[:, :, :3], [65536.0, 256.0, 1.0])
    	normalized_depth /= 16777215.0  # (256.0 * 256.0 * 256.0 - 1.0)
	return normalized_depth 

def color_to_depth(image):

	# depth_map_array = carla.image_converter.depth_to_logarithmic_grayscale(dept_map_image)	
	
	# scipy.misc.imsave(depth_map_array)
	
	normalized_depth = depth_to_array(image)
	
	logdepth = numpy.ones(normalized_depth.shape) + (numpy.log(normalized_depth) / 5.70378)
    	logdepth = numpy.clip(logdepth, 0.0, 1.0)
	logdepth *= 255.0
	
	depth_map_array = numpy.repeat(logdepth[:, :, numpy.newaxis], 3, axis=2)
	
	frame = image.frame_number
	address = '/home/kishor/GWM/Carla_Sim/depth_output/%0.6d.png' % frame
	
	scipy.misc.imsave(address, depth_map_array)

def main():
	
	try:
		client = carla.Client('localhost', 2000)
		client.set_timeout(10.0) # seconds
		world = client.get_world()
		blueprint_library = world.get_blueprint_library()
		vehicles = blueprint_library.filter('vehicle.*')
		# print(vehicles)
		ego_vehicle = world.get_actors().filter('vehicle.*')
		print(ego_vehicle)

		for actor in ego_vehicle:
			print(actor)
			ego_vehicle = actor

		print(ego_vehicle.get_location())

		camera_rgb = world.get_blueprint_library().find('sensor.camera.depth')
		camera_rgb.set_attribute('image_size_x', '1920')
		camera_rgb.set_attribute('image_size_y', '1080')
		camera_rgb.set_attribute('fov', '110')
		transform = carla.Transform(carla.Location(x=0.8, z=1.7))
		camera_rgb_attach = world.spawn_actor(camera_rgb, transform, attach_to=ego_vehicle)

		# camera_rgb_attach.listen(lambda image: image.save_to_disk('depth_output/%06d.png' % image.frame_number))
		
		# camera_rgb_attach.listen(lambda image: image.save_to_disk('depth_output/%06d.png' % image.frame_number))
		
		camera_rgb_attach.listen(lambda image: color_to_depth(image))
		
		
		# print(image)
		
		# lambda image: image.save_to_disk('depth_output/%06d.png' % image.frame_number)
		
		print("Save image")


		while True:
			time.sleep(1)
	
	finally:
		print("Finally..!!!")


if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        print('\ndone.')

