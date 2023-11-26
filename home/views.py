from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import logout
import subprocess,time

# Create your views here.


def home(request):
    context={
        'page':'Home'
    }
    return render(request,'index.html',context)

def logOut(request):
    logout(request)
    return redirect('/login/')

# def roscoreStart(request):
#     subprocess.call(['gnome-terminal', '--', 'bash', '-c', 'roscore'],0)
#     time.sleep(2)
#     subprocess.call(['gnome-terminal', '--', 'bash', '-c', 'rosrun turtlesim turtlesim_node '],0)
#     subprocess.call(['gnome-terminal', '--', 'bash', '-c', 'rosrun turtlesim turtle_teleop_key'],0)
#     # time.sleep(5)

#     # # Send an additional command to the first terminal
#     # additional_command = 'kill {}'.format(process.pid)
#     # print(additional_command)
#     # subprocess.call(['gnome-terminal', '--', 'bash', '-c', f'echo {additional_command} > /proc/{process.pid}/fd/0'])

#     return redirect('/')