from .tasks import send_img


localpath = 'img.geit.jpg'
path = 'img.geit.png'

send_img.apply_async(args=[localpath,path],ignore_result=True)

print('Start upload')