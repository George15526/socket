import threading, socket, time
from user.models import Users
global males, females
males = []
females = []
lock = threading.Lock()


''' 從資料庫欄位內容取得使用者性別'''
def getGender(userid):
   user = Users.query.filter_by(id=id).first() 
   if user:
       return user.gender #值根據資料庫不同
   else:
       return None

def pair_users(userid): 
    gender = getGender(userid)
    if gender == 'male':
        males.append(userid)
    elif gender == 'female':
        females.append(userid)
        
    start_time = time.time()
    while True:
        if len(females) > 0 and len(males) > 0:
            m = males.pop(0)
            f = females.pop(0)
            if gender == 'male': 
                return f
            else:
                return m
        elif time.time() - start_time > 30 * 60:  
            return 'failed'
        else:
            time.sleep(1) 
