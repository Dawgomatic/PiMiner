import os

def init_function():
    os.system('sudo apt update -y') 
    os.system('sudo apt upgrade -y ') 
    os.system('sudo apt install git automake autoconf libcurl4-openssl-dev libjansson-dev libssl-dev libgmp-dev') 
    
def mine_init():    
    os.system('cd /opt')   
    os.system('sudo git clone https://github.com/tpruvot/cpuminer-multi') 
    os.system('cd cpuminer-multi') 
    os.system('sudo ./autogen.sh') 
    os.system('sudo ./configure') 
    os.system('sudo ./build.sh') 
     
init_function()
mine_init()
