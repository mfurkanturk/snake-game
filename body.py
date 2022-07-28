
def drawBody(score, ):               #TODO: Her turda tekrar cizilecek body, skor miktari kadar 
    location = []
    location[0] = [1, 2]
    
    return location


def bodyCol(location):                #TODO: Bir sonraki adimda yilanin basi body olan bir kareye geliyorsa end fonksiyonunu cagir   
    for i in range(len(location)):
        if location[0] == location[i]:
            endgame()                 #! Endgame function will be here
            
