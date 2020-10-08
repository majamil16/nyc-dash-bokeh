

login_url="/login"

def get_user(request):
    
    usn = request.get_argument("username")
    pw = request.get_argument("password")
    
    if(usn == "nyc" and pw == "iheartnyc"):
        return 1
    else:
        return None




