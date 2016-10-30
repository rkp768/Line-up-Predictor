import csv,random,sys
from sklearn import linear_model
from sklearn.svm import SVR
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from itertools import combinations as C

sys.argv[1] = 'AUS'
f1 = open("Indiabatting.csv","r")
f2 = open("indiabowling.csv","r")
f3 = open("dataset.csv","w")
batting = csv.reader(f1)
bowling = csv.reader(f2)
data = csv.writer(f3)

against = ["WI","AUS","PAK","ZIM","SL","NZ","EN","BAN"]

attr_bat = []
attr_bowl = []

dic_bat = {}
dic_bowl = {}

batsmen = []
for i in batting:
	attr_bat.append(i)
	break
attr_bat = attr_bat[0]    #create dictionary
for i in batting:	
	batsmen.append(i[0])
	for k in zip(attr_bat[1:],i[1:]):
		dic_bat[k[0]+'_'+i[0]] = k[1]

bowler = []
for i in bowling:
	attr_bowl.append(i)
	break
attr_bowl = attr_bowl[0]
for i in bowling:
	bowler.append(i[0])
	for k in zip(attr_bowl[1:],i[1:]):
		dic_bowl[k[0]+'_'+i[0]] = k[1]

temp = (set(bowler) & set(batsmen))
bowler = list(set(bowler) - temp)
batsmen = list(set(batsmen) - temp)
data.writerow(['p'+str(i) for i in range(1,12)]+["WI","AUS","PAK","ZIM","SL","NZ","EN","BAN"])
for i in range(500):
	data.writerow(random.sample(batsmen, 6) + random.sample(bowler, 5) + [int(100*random.random())*0.01 for i in range(8)])
f3.close()

for degree in [1,2]:
    f3 = open("dataset.csv","r")
    data = csv.reader(f3)
    data.next()
    modelbaavg = make_pipeline(PolynomialFeatures(degree), Ridge())
    modelbarun = make_pipeline(PolynomialFeatures(degree), Ridge())
    modelbacen = make_pipeline(PolynomialFeatures(degree), Ridge())
    modelbahac = make_pipeline(PolynomialFeatures(degree), Ridge())
    modelbanot = make_pipeline(PolynomialFeatures(degree), Ridge())
    modelbahig = make_pipeline(PolynomialFeatures(degree), Ridge())
    modelboavg = make_pipeline(PolynomialFeatures(degree), Ridge())
    modelbowic = make_pipeline(PolynomialFeatures(degree), Ridge())
    modelboeco = make_pipeline(PolynomialFeatures(degree), Ridge())
    modelbowpi = make_pipeline(PolynomialFeatures(degree), Ridge())
    modelbofwi = make_pipeline(PolynomialFeatures(degree), Ridge())
    modelbotwm = make_pipeline(PolynomialFeatures(degree), Ridge())
    train_in_ba_avg = []
    train_in_ba_run = []
    train_in_ba_cen = []
    train_in_ba_hac = []
    train_in_ba_not = []
    train_in_ba_hig = []
    train_in_bo_avg = []
    train_in_bo_wic = []
    train_in_bo_eco = []
    train_in_bo_wpi = []
    train_in_bo_fwi = []
    train_in_bo_twm = []
    train_out = []
    test_in_ba_avg = []
    test_in_ba_run = []
    test_in_ba_cen = []
    test_in_ba_hac = []
    test_in_ba_not = []
    test_in_ba_hig = []
    test_in_bo_avg = []
    test_in_bo_wic = []
    test_in_bo_eco = []
    test_in_bo_wpi = []
    test_in_bo_fwi = []
    test_in_bo_twm = []
    test_out = []

    cnt = 0
    for i in data:
        if cnt<400:
            train_in_ba_avg.append([float(dic_bat['Average_'+x]) for x in i[0:6]])
            train_in_ba_run.append([float(dic_bat['Runs_'+x]) for x in i[0:6]])
            train_in_ba_cen.append([float(dic_bat['Centuries_'+x]) for x in i[0:6]])
            train_in_ba_hac.append([float(dic_bat['Half Centuries_'+x]) for x in i[0:6]])
            train_in_ba_not.append([float(dic_bat['Not Out_'+x]) for x in i[0:6]])
            train_in_ba_hig.append([float(dic_bat['Highest Score_'+x]) for x in i[0:6]])
            train_in_bo_avg.append([float(dic_bowl['Average_'+x]) for x in i[6:11]])
            train_in_bo_wic.append([float(dic_bowl['Wickets_'+x]) for x in i[6:11]])
            train_in_bo_eco.append([float(dic_bowl['Economy Rate_'+x]) for x in i[6:11]])
            train_in_bo_wpi.append([float(dic_bowl['Wickt/Inning_'+x]) for x in i[6:11]])
            train_in_bo_fwi.append([float(dic_bowl['5 W I_'+x]) for x in i[6:11]])
            train_in_bo_twm.append([float(dic_bowl['10 W M_'+x]) for x in i[6:11]])
            train_out.append(float(i[11 + against.index(sys.argv[1])]))
        else:
            test_in_ba_avg.append([float(dic_bat['Average_'+x]) for x in i[0:6]])
            test_in_ba_run.append([float(dic_bat['Runs_'+x]) for x in i[0:6]])
            test_in_ba_cen.append([float(dic_bat['Centuries_'+x]) for x in i[0:6]])
            test_in_ba_hac.append([float(dic_bat['Half Centuries_'+x]) for x in i[0:6]])
            test_in_ba_not.append([float(dic_bat['Not Out_'+x]) for x in i[0:6]])
            test_in_ba_hig.append([float(dic_bat['Highest Score_'+x]) for x in i[0:6]])
            test_in_bo_avg.append([float(dic_bowl['Average_'+x]) for x in i[6:11]])
            test_in_bo_wic.append([float(dic_bowl['Wickets_'+x]) for x in i[6:11]])
            test_in_bo_eco.append([float(dic_bowl['Economy Rate_'+x]) for x in i[6:11]])
            test_in_bo_wpi.append([float(dic_bowl['Wickt/Inning_'+x]) for x in i[6:11]])
            test_in_bo_fwi.append([float(dic_bowl['5 W I_'+x]) for x in i[6:11]])
            test_in_bo_twm.append([float(dic_bowl['10 W M_'+x]) for x in i[6:11]])
            test_out.append(float(i[11 + against.index(sys.argv[1])]))
        cnt += 1
    modelbaavg.fit(train_in_ba_avg, train_out)
    modelbarun.fit(train_in_ba_run, train_out)
    modelbacen.fit(train_in_ba_cen, train_out)
    modelbahac.fit(train_in_ba_hac, train_out)
    modelbanot.fit(train_in_ba_not, train_out)
    modelbahig.fit(train_in_ba_hig, train_out)
    
    modelboavg.fit(train_in_bo_avg, train_out)
    modelbowic.fit(train_in_bo_wic, train_out)
    modelboeco.fit(train_in_bo_eco, train_out)
    modelbowpi.fit(train_in_bo_wpi, train_out)
    modelbofwi.fit(train_in_bo_fwi, train_out)
    modelbotwm.fit(train_in_bo_twm, train_out)
    i=0
    errbaavg = 0
    errbarun = 0
    errbacen = 0
    errbahac = 0
    errbanot = 0
    errbahig = 0
    errboavg = 0
    errbowic = 0
    errboeco = 0
    errbowpi = 0
    errbofwi = 0
    errbotwm = 0
    while(i<len(test_out)):
        opbaavg = modelbaavg.predict([x for x in test_in_ba_avg[i][0:6]])[0]
        opbarun = modelbarun.predict([x for x in test_in_ba_run[i][0:6]])[0]
        opbacen = modelbacen.predict([x for x in test_in_ba_cen[i][0:6]])[0]
        opbahac = modelbahac.predict([x for x in test_in_ba_hac[i][0:6]])[0]
        opbanot = modelbanot.predict([x for x in test_in_ba_not[i][0:6]])[0]
        opbahig = modelbahig.predict([x for x in test_in_ba_hig[i][0:6]])[0]
        opboavg = modelboavg.predict([x for x in test_in_bo_avg[i][0:6]])[0]
        opbowic = modelbowic.predict([x for x in test_in_bo_wic[i][0:6]])[0]
        opboeco = modelboeco.predict([x for x in test_in_bo_eco[i][0:6]])[0]
        opbowpi = modelbowpi.predict([x for x in test_in_bo_wpi[i][0:6]])[0]
        opbofwi = modelbofwi.predict([x for x in test_in_bo_fwi[i][0:6]])[0]
        opbotwm = modelbotwm.predict([x for x in test_in_bo_twm[i][0:6]])[0]
        errbaavg += (opbaavg - float(test_out[i]))**2
        errbarun += (opbarun - float(test_out[i]))**2
        errbacen += (opbacen - float(test_out[i]))**2
        errbahac += (opbahac - float(test_out[i]))**2
        errbanot += (opbanot - float(test_out[i]))**2
        errbahig += (opbahig - float(test_out[i]))**2
        errboavg += (opboavg - float(test_out[i]))**2
        errbowic += (opbowic - float(test_out[i]))**2
        errboeco += (opboeco - float(test_out[i]))**2
        errbowpi += (opbowpi - float(test_out[i]))**2
        errbofwi += (opbofwi - float(test_out[i]))**2
        errbotwm += (opbotwm - float(test_out[i]))**2
        i += 1
    print "Error Estimate Batsmen avg = ",(errbaavg*1.0/len(test_out))**0.5
    print "Error Estimate Bowler avg = ",(errboavg*1.0/len(test_out))**0.5
    print "Error Estimate Batsmen runs = ",(errbarun*1.0/len(test_out))**0.5
    print "Error Estimate Bowler wickets = ",(errbowic*1.0/len(test_out))**0.5
    print "Error Estimate Batsmen centuries = ",(errbacen*1.0/len(test_out))**0.5
    print "Error Estimate Bowler economy = ",(errboeco*1.0/len(test_out))**0.5
    print "Error Estimate Batsmen half-centuries = ",(errbahac*1.0/len(test_out))**0.5
    print "Error Estimate Bowler wickets per innings = ",(errbowpi*1.0/len(test_out))**0.5
    print "Error Estimate Batsmen not-outs = ",(errbanot*1.0/len(test_out))**0.5
    print "Error Estimate Bowler 5-wicket halls = ",(errbofwi*1.0/len(test_out))**0.5
    print "Error Estimate Batsmen highest score = ",(errbahig*1.0/len(test_out))**0.5
    print "Error Estimate Bowler 10-wicket halls = ",(errbotwm*1.0/len(test_out))**0.5
    f3.close()

print "team prediction starts"
print "**********************"
allbats = list(C(random.sample(batsmen, 8),6))
allbowl = list(C(random.sample(bowler, 7),5))
print "**********************"
print "batsmen"
temp = []
temp2= []
for i in allbats:
	arr = [float(dic_bat['Average_'+x]) for x in i] 
	temp2.append(modelbaavg.predict(arr)[0])
i=0
while(i<len(temp2)):
	if (temp2[i] >= sum(temp2)/len(temp2)):
		temp.append(allbats[i])
	i+=1
allbats = temp
for i in allbats:
	print i
print "bowler"
temp = []
temp2= [] 
for i in allbowl:
	arr = [float(dic_bowl['Average_'+x]) for x in i] 
	temp2.append(modelboavg.predict(arr)[0])
i=0
while(i<len(temp2)):
	if (temp2[i] >= sum(temp2)/len(temp2)):
		temp.append(allbowl[i])
	i+=1
allbowl = temp
for i in allbowl:
	print i
print "*************************************"
print "batsmen"
temp = []
temp2= []
for i in allbats:
	arr = [float(dic_bat['Highest Score_'+x]) for x in i] 
	temp2.append(modelbahig.predict(arr)[0])	
i=0
while(i<len(temp2)):
	if (temp2[i] >= sum(temp2)/len(temp2)):
		temp.append(allbats[i])
	i+=1
allbats = temp
for i in allbats:
	print i
print "bowler"
temp = []
temp2= [] 
for i in allbowl:
	arr = [float(dic_bowl['Wickets_'+x]) for x in i] 
	temp2.append(modelbowic.predict(arr)[0])
i=0
while(i<len(temp2)):
	if (temp2[i] >= sum(temp2)/len(temp2)):
		temp.append(allbowl[i])
	i+=1
allbowl = temp
for i in allbowl:
	print i
print "*************************************"
print "batsmen"
temp = []
temp2= []
for i in allbats:
	arr = [float(dic_bat['Runs_'+x]) for x in i] 
	temp2.append(modelbarun.predict(arr)[0])	
i=0
while(i<len(temp2)):
	if (temp2[i] >= sum(temp2)/len(temp2)):
		temp.append(allbats[i])
	i+=1
allbats = temp
for i in allbats:
	print i
print "bowler"
temp = []
temp2= [] 
for i in allbowl:
	arr = [float(dic_bowl['Economy Rate_'+x]) for x in i] 
	temp2.append(modelboeco.predict(arr)[0])
i=0
while(i<len(temp2)):
	if (temp2[i] >= sum(temp2)/len(temp2)):
		temp.append(allbowl[i])
	i+=1
allbowl = temp
for i in allbowl:
	print i
print "*************************************"
print "batsmen"
temp = []
temp2= []
for i in allbats:
	arr = [float(dic_bat['Half Centuries_'+x]) for x in i] 
	temp2.append(modelbahac.predict(arr)[0])	
i=0
while(i<len(temp2)):
	if (temp2[i] >= sum(temp2)/len(temp2)):
		temp.append(allbats[i])
	i+=1
allbats = temp
for i in allbats:
	print i
print "bowler"
temp = []
temp2= [] 
for i in allbowl:
	arr = [float(dic_bowl['Wickt/Inning_'+x]) for x in i] 
	temp2.append(modelbowpi.predict(arr)[0])
i=0
while(i<len(temp2)):
	if (temp2[i] >= sum(temp2)/len(temp2)):
		temp.append(allbowl[i])
	i+=1
allbowl = temp
for i in allbowl:
	print i
print "*************************************"
print "batsmen"
temp = []
temp2= []
for i in allbats:
	arr = [float(dic_bat['Not Out_'+x]) for x in i] 
	temp2.append(modelbanot.predict(arr)[0])	
i=0
while(i<len(temp2)):
	if (temp2[i] >= sum(temp2)/len(temp2)):
		temp.append(allbats[i])
	i+=1
allbats = temp
for i in allbats:
	print i
print "bowler"
temp = []
temp2= [] 
for i in allbowl:
	arr = [float(dic_bowl['5 W I_'+x]) for x in i] 
	temp2.append(modelbofwi.predict(arr)[0])
i=0
while(i<len(temp2)):
	if (temp2[i] >= sum(temp2)/len(temp2)):
		temp.append(allbowl[i])
	i+=1
allbowl = temp
for i in allbowl:
	print i
print "*************************************"
print "batsmen"
temp = []
temp2= []
for i in allbats:
	arr = [float(dic_bat['Centuries_'+x]) for x in i] 
	temp2.append(modelbacen.predict(arr)[0])	
i=0
while(i<len(temp2)):
	if (temp2[i] >= sum(temp2)/len(temp2)):
		temp.append(allbats[i])
	i+=1
allbats = temp
for i in allbats:
	print i
print "bowler"
temp = []
temp2= [] 
for i in allbowl:
	arr = [float(dic_bowl['10 W M_'+x]) for x in i] 
	temp2.append(modelbotwm.predict(arr)[0])
i=0
while(i<len(temp2)):
	if (temp2[i] >= sum(temp2)/len(temp2)):
		temp.append(allbowl[i])
	i+=1
allbowl = temp
for i in allbowl:
	print i
print "*************************************"

f1.close()
f2.close()
