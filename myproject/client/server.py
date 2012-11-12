from bottle import route, run, request, post
import logging
import os
import subprocess
import threading
import urllib2
#Change to work to have this running on indiv client machines, instead of commanding all machines.

logger = logging.getLogger("soap")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("soap.log")
handler.setLevel(logging.INFO)
logger.addHandler(handler)

@route('/hello/:name')
def index(name='World'):
    return template('<b>Hello {{name}}</b>!', name=name)


class SoapServer():

	def __new__(self, *args, **kwargs):
		#Do routes here.
		obj = super(SoapServer, self).__new__(self,*args, **kwargs)
		route("/play/:stream")(obj.playStream)
		return obj

	def __init__(self, port, timeout=20):
		"""
        Create a new SOAP REST Server

        :type port: int
        :param port: port to listen for requests on

        :type bathrooms: dict
        :param bathrooms: A dict mapping bathroom names to sound devices

        :type timeout: int
        :param timeout: time in minutes to wait before killing a stream
        """
        # self.port = port
        # self.timeout = timeout * 60
        # self.command_string = "vlc"
        # self.locks = {}
        # self.currently_playing = {}
        # logger.info("Init soap.")

def onExit():
	urllib2.urlopen("http://play-soap.csh.rit.edu:6544/nextSong/")

def popenAndCall(onExit, popenArgs):
    """
    Runs the given args in a subprocess.Popen, and then calls the function
    onExit when the subprocess completes.
    onExit is a callable object, and popenArgs is a list/tuple of args that 
    would give to subprocess.Popen.
    """
    def runInThread(onExit, popenArgs):
        proc = subprocess.Popen(popenArgs)
        print proc.wait()
        onExit()
        return
    thread = threading.Thread(target=runInThread, args=(onExit, popenArgs))
    thread.start()
    # returns immediately after the thread starts
    return thread

@post('/play/')
def playStream():
	stream = str(request.body.read())
	stream = urllib2.unquote(stream)
	print(stream)
	stream = stream.split('=', 1)[1]
	print(stream)
	#stream = stream[:len(stream) - 1]
	#stream = '"' + stream + '"'
	commandArray = ["mplayer", "-ao", "pulse:localhost", stream]
	#commandArray = ["//Applications//VLC.app//Contents//MacOS//VLC", "-Irc" ,stream]
	print (commandArray)
	popenAndCall(onExit, commandArray)
	#subprocess.Popen(commandArray, stdin=subprocess.PIPE)

run(host='129.21.50.217', port=8082)
