"""Your awesome Distance Vector router for CS 168."""

import sim.api as api
import sim.basics as basics

# We define infinity as a distance of 16.
INFINITY = 16


class DVRouter(basics.DVRouterBase):
    # NO_LOG = True # Set to True on an instance to disable its logging
    # POISON_MODE = True # Can override POISON_MODE here
    # DEFAULT_TIMER_INTERVAL = 5 # Can override this yourself for testing

    def __init__(self):
        """
        Called when the instance is initialized.

        You probably want to do some additional initialization here.

        """
        self.cv = {} # distance vector
        self.rt = {}
        self.route = {}
        self.allEntity = set()
        self.start_timer()  # Starts calling handle_timer() at correct rate

    def handle_link_up(self, port, latency):
        """
        Called by the framework when a link attached to this Entity goes up.

        The port attached to the link and the link latency are passed
        in.

        """
        # self.cv[]
        print("attached link")
        pass


    def handle_link_down(self, port):
        """
        Called by the framework when a link attached to this Entity does down.

        The port number used by the link is passed in.

        """
        print(self.name + ": " + str(port))
        pass

    def handle_rx(self, packet, port):
        """
        Called by the framework when this Entity receives a packet.

        packet is a Packet (or subclass).
        port is the port number it arrived on.

        You definitely want to fill this in.

        """
        if isinstance(packet, basics.RoutePacket):
            print(packet)
            pass
        elif isinstance(packet, basics.HostDiscoveryPacket):
            if packet.src.name in self.cv and self.cv[packet.src.name] == port:
                return
            self.cv[packet.src.name] = port
            self.updateDV()
        else:
            # Totally wrong behavior for the sake of demonstration only: send
            # the packet back to where it came from!
            print(packet, port)
            if packet.dst.name in self.route:
                outport = self.route[packet.dst.name]
                self.send(packet, port=outport)

    def updateDV(self):
        self.route = self.cv

    def handle_timer(self):
        """
        Called periodically.

        When called, your router should send tables to neighbors.  It
        also might not be a bad place to check for whether any entries
        have expired.

        """
        pass
