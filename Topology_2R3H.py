from mininet.net import Mininet
from mininet.node import Node, OVSKernelSwitch, Controller, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.topo import Topo
from mininet.log import setLogLevel, info
import argparse


class LinuxRouter( Node ):
    "A Node with IP forwarding enabled."

    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        # Enable forwarding on the router
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()
        
class MyTopo( Topo ):

    def __init__( self ):

        # Initialize topology
        Topo.__init__( self )

        #s1 = net.addSwitch ( 's1' )
        r1 = self.addNode( 'r1' ,cls=LinuxRouter, ip='192.168.1.2/24' )
        r2 = self.addNode( 'r2' ,cls=LinuxRouter, ip='192.168.1.3/24' )
        h1 = self.addHost( 'h1' , ip='192.168.1.1/24', defaultRoute= 'via 192.168.1.2')
        h2 = self.addHost( 'h2' , ip='192.168.2.1/24', defaultRoute= 'via 192.168.2.2')
        h3 = self.addHost( 'h3' , ip='192.168.3.1/24', defaultRoute= 'via 192.168.3.2')

        #Establishing the links from hosts to routers
        info( "Creating links\n" )
        self.addLink( h1, r1 )
        self.addLink( h2, r1, intfName2='r1-eth1', params2={'ip' : '192.168.2.2/24' } )
        self.addLink( r2, r1, intfName2='r1-eth2', params2={'ip' : '192.168.3.3/24' } )
        self.addLink( h3, r2, intfName2='r2-eth1', params2={'ip' : '192.168.3.2/24' } )
    
     

        
     
topos = { 'mytopo': ( lambda: MyTopo() ) }

