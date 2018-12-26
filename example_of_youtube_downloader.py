u1 = ['https://youtu.be/q2cHGd_MP_4',
'https://youtu.be/ZAZNrW992Fc',
'https://youtu.be/pklIkeuveOE',
'https://youtu.be/60ug2YVjdhU',
'https://youtu.be/ekJCcJjyLAI',
'https://youtu.be/zJljSLqUbUc',
'https://youtu.be/friM7GDOcD0',
'https://youtu.be/CASxP2Pldmk',
'https://youtu.be/q0cVDeluL3c',
'https://youtu.be/YiBwYemQajA',
'https://youtu.be/YjUPiMY8nSs',
'https://youtu.be/03ckSzMreeM',
'https://youtu.be/lVeROX4Mkv8',
'https://youtu.be/dTPwQEegHxw']
u2 = ['https://youtu.be/P4-CFlsBZCU',
'https://youtu.be/6E9S3PoeNV4',
'https://youtu.be/Ixse7rx8Vf0',
'https://youtu.be/snQLH-KzpLY',
'https://youtu.be/sn2wDa6SI_E',
'https://youtu.be/PPO1xs64Xgg',
'https://youtu.be/nsKdFJipGO4',
'https://youtu.be/GDRUJsYjPl8',
'https://youtu.be/AkHyqqf-rQs',
'https://youtu.be/mqr5oANeEI8',
'https://youtu.be/v4k4ep3lSwc',
'https://youtu.be/Bbn_sSLenYk',
'https://youtu.be/VvrecTHAWRU',
'https://youtu.be/yXV15izY1dQ',
'https://youtu.be/Ac8KiNC0zM0',
'https://youtu.be/i9dtA6VZ8u0',
'https://youtu.be/EsEogLmLcuY',
'https://youtu.be/tQG26uPoCcA',
'https://youtu.be/3mFTpJHHzWA',
'https://youtu.be/0WVRMlRn57U',
'https://youtu.be/HeWFwYt8i-o',
'https://youtu.be/M7dy4gId_wA',
'https://youtu.be/oQJBtVP95c8',
'https://youtu.be/xvPdi6gjDMA',
'https://youtu.be/VRhrAUT602I',
'https://youtu.be/tlHa2sm1uDg']
u3 = ['https://youtu.be/3yw8qFB2SJ8',
'https://youtu.be/xXFXHfGrCkI',
'https://youtu.be/pSLx0keOU0U',
'https://youtu.be/9pNcPbGBuFg',
'https://youtu.be/g0JZEOZPITo',
'https://youtu.be/wbiZIz76rRo',
'https://youtu.be/hEACL6xJ1ts',
'https://youtu.be/ig7ztHAd2J4',
'https://youtu.be/lP-ZNoHbBEc',
'https://youtu.be/ECVlamfF__w',
'https://youtu.be/Udc_2z-pL9Y',
'https://youtu.be/tvZ-Hsy_riA']
u4 = ['https://youtu.be/61D7D0Df6QY',
'https://youtu.be/--IOdbXnML8',
'https://youtu.be/l2f743SpPiw',
'https://youtu.be/La49EMG5Ar4',
'https://youtu.be/vokziIl_3Eo',
'https://youtu.be/_fwDUx5JpH8',
'https://youtu.be/TRsSsOruga4',
'https://youtu.be/PtUpe1Vj264',
'https://youtu.be/Eih56jZ3bcA',
'https://youtu.be/wCvxYC_RgI8',
'https://youtu.be/Xa9tPXx8SSk',
'https://youtu.be/jmV3UFDJRYc',
'https://youtu.be/PmntI1GRh9c',
'https://youtu.be/8xcj1ejMbGA',
'https://youtu.be/a9jx_-NWkl0',
'https://youtu.be/xB-G8zmwghA',
'https://youtu.be/AcujBxMJhO4',
'https://youtu.be/yn6yjk_sI_g',
'https://youtu.be/fyno3uRscVA',
'https://youtu.be/uoUdgF4l3zM',
'https://youtu.be/wXDST5kWIrY',
'https://youtu.be/4KwBBAmAlSs',
'https://youtu.be/-5ISDiAQjfQ',
'https://youtu.be/2rCLVQyiOOo',
'https://youtu.be/X1ZPCmw6rkA',
'https://youtu.be/wt_mIBXq654',
'https://youtu.be/I_njPcYRDXs',
'https://youtu.be/gIGsMLawD0E',
'https://youtu.be/8EA5suZ3vIc',
'https://youtu.be/BsYl0yUU4qM',
'https://youtu.be/vB6EKsX12hc',
'https://youtu.be/0_ISFJYgeSo',
'https://youtu.be/kHc_RUqHLx4',
'https://youtu.be/L1aqKuoI8Xw',
'https://youtu.be/ASqK_pZpd5s',
'https://youtu.be/Q6TzetFl_9E',
'https://youtu.be/b7KNIA4w9lE',
'https://youtu.be/_V8vki6W0w0',
'https://youtu.be/F12MUsgpFA0',
'https://youtu.be/kn7aL4zwROY',
'https://youtu.be/f1GYgMLzdHE',
'https://youtu.be/MmkSu3GRd2Q']


from pytube import YouTube
all_names = []



d = {}
counter = 0
lins_qty = sum([len(i) for i in [u1, u2, u3, u4]])
for unit in [u1, u2, u3, u4]:
	for link in unit:
		counter += 1
		print(counter, '\t', lins_qty - counter, '\t', counter / lins_qty)
		try:
			name = YouTube(link).title#.streams.filter(subtype='mp4').all()[0].download()
			d[link] = name
			all_names.append(name)
		except:
			d[link] = 'error'
			all_names.append(link + ' Error occured')


if 'error' in d.values():
	print("##################################################################################################################################")
	print("there is () failiers".format(len([i for i in d if d[i] == 'error'])))
	
	ls = [i for i in d if d[i] == 'error']
	d2 = {}
	counter = 0
	lins_qty = len(ls)
	for link in ls:
		counter += 1
		print(counter, '\t', lins_qty - counter, '\t', counter / lins_qty)
		try:
			name = YouTube(link).title#.streams.filter(subtype='mp4').all()[0].download()
			d2[link] = name
			all_names.append(name)
		except:
			d2[link] = 'error'
			all_names.append(link + ' Error occured')

import pickle
try:
	with open("d.pkl", "wb") as file:
		pickle.dump(d, file)
	try:
		with open("d2.pkl", "wb") as file:
			pickle.dump(d2, file)
	except:
		pass
	with open("all_names.pkl", "wb") as file:
		pickle.dump(all_names, file)
	try:
		!poweroff
	except:
		import os
		os.system('poweroff')
except:
	print("\n\n\n\n\n THERE IS AN ERRORs")