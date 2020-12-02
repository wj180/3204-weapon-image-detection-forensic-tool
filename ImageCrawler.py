from simple_image_download import simple_image_download as simp

response = simp.simple_image_download

response().download('grenade', 100)

print(response().urls('grenade', 100))