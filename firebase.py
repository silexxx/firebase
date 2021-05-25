import pyrebase
import glob


config={}


firebase=pyrebase.initialize_app(config)
storage=firebase.storage()


images_path=glob.glob("images/*.png")
print(images_path)

for i in images_path:
    temp=i.split("/")[1]
    path_on_cloud=f"images/{temp}"
    path_local=f"images/{temp}"
    storage.child(path_on_cloud).put(path_local)
    url=storage.child(f"images/{temp}").get_url(None)
    print(url)