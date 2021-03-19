  
import os

def auto():
    os.system('/opt/cpuminer-multi/cpuminer -a cryptonight -o stratum+tcp://xmr.pool.minergate.com:45700 -u jeremyruroede@gmail.com') #monero
    #os.system('/opt/cpuminer-multi/cpuminer -a cryptonight -o stratum+tcp://xeth.pool.minergate.com:45791 -u jeremyruroede@gmail.com') #etherium
    #os.system('/opt/cpuminer-multi/cpuminer -a cryptonight -o stratum+tcp://ltc.pool.minergate.com:3336 -u jeremyruroede@gmail.com') #litecoin
    
auto()
