from gallery.models import Sample, Prototype
import os

dir = "gallery/static/img/"

i = 1
j = 1
for path in os.listdir(dir): 
    full_path = os.path.join(dir,path)
    if "7560" in path:
        Prototype.objects.create(title = 'Prototype {}'.format(i), image=path, description='Prototype size: 256x256. \n Prototype from iteration 7560')
        i+=1
    if "8060" in path:
        Prototype.objects.create(title = 'Prototype {}'.format(i), image=path, description='Prototype size: 256x256. \n Prototype from iteration 8060')
        i+=1
    if "sample" in path:
        if int(path[7]) <= 8 and path[6] =="0":
            Sample.objects.create(title = 'Sample {}'.format(j), image=path, description='Sample size: 256x256. \n Selected sample from iteration 7560')
            j+=1
        else:
            Sample.objects.create(title = 'Sample {}'.format(j), image=path, description='Sample size: 256x256. \n Selected sample from iteration 8060')
            j+=1






# sample_counter = 0
# for path in os.listdir(dir):
#     full_path = os.path.join(dir,path)
  
#     if path == "collection7560":
#         proto_counter = 0
#         print("-------------" + path)
#         for im in os.listdir(full_path):
#             if "ss" not in im:
#                 print("rename " + os.path.join(full_path,im) + "to --- " + os.path.join(full_path,"it7560_{}.png".format(proto_counter)))
#                 os.rename(os.path.join(full_path,im),os.path.join(full_path,"proto7560_{}.png".format(proto_counter)))
#                 proto_counter +=1
#             # else:
#             #     print(os.path.join(full_path,"sample7560_{}".format(sample_counter)))
#             #     os.rename(os.path.join(full_path,im),os.path.join(full_path,"sample7560_{}.png".format(sample_counter)))
#             #     sample_counter +=1
#     if path == "collection8060":
#         proto_counter = 0
#         print("---------" + path)
#         for im in os.listdir(full_path):
#             if "ss" not in im:
#                 print("rename " + os.path.join(full_path,im) + "--- to ---" + os.path.join(full_path,"it8060_{}.png".format(proto_counter)))
#                 os.rename(os.path.join(full_path,im),os.path.join(full_path,"proto8060_{}.png".format(proto_counter)))
#                 proto_counter +=1
#             # else:
#             #     print(os.path.join(full_path,"sample8060_{}".format(sample_counter)))
#             #     os.rename(os.path.join(full_path,im),os.path.join(full_path,"sample8060_{}.png".format(sample_counter)))
#             #     sample_counter +=1
                
        
# for path in os.listdir(dir):
#     full_path = os.path.join(dir, path)
#     if os.path.isdir(full_path):
#         if path == "gallery":
#             i = 1 
#             for subpath in os.listdir(full_path):
#                 full_subpath = os.path.join(full_path, subpath)
#                 if subpath == "7560":
#                     for spath in os.listdir(full_subpath): 
#                         print(os.path.join(dir,spath))
#                         Sample.objects.create(title = 'Sample {}'.format(i), image=os.path.join(dir,spath), description='Sample size: 256x256. \n Selected sample from iteration 7560')
#                         i += 1
#                 if subpath == "8060":
#                     for spath in os.listdir(full_subpath):
#                         print(os.path.join(dir,spath))
#                         Sample.objects.create(title = 'Sample {}'.format(i), image=os.path.join(dir,spath), description='Sample size: 256x256. \n Selected sample from iteration 8060')
#                         print(spath)
#                         i +=1
#         i = 1 
#         if path == "collection7560":
#             for subpath in os.listdir(full_path):
#                 full_subpath = os.path.join(full_path, subpath) 
#                 print(full_subpath)
#                 Prototype.objects.create(title = 'Prototype {}'.format(i), image=full_subpath, description='Prototype size: 256x256. \n Prototype from iteration 7560')
#                 i += 1
#         if path == "collection8060":
#             for subpath in os.listdir(full_path):
#                 full_subpath = os.path.join(full_path, subpath) 
#                 print(full_subpath)
#                 # Prototype.objects.create(title = 'Prototype {}'.format(i), image=full_subpath, description='Prototype size: 256x256. \n Prototype from iteration 8060')
#                 i += 1
                
    



# for i in range(101,121):
#     Sample.objects.create(title = 'Sample {}'.format(i-100), image='img/seed0{}.png'.format(i), description='Sample size: 256x256.')

# for i in range(10,99):
#     Prototype.objects.create(title = 'Prototype {}'.format(i-9), image='protoimg/seed00{}.png'.format(i), description='Sample size: 256x256.')

