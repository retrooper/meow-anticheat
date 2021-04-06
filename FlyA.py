from packetevents import PacketEvents
from packetevents import Player
from packetevents import Packet
class PacketListener {
  def on_packet_play_receive(Player player, Packet packet):
    if player.y is greater than 256:
       player.kick("You are hacking! Fly A detection Meow anticheat!")
}

def onEnable():
  priority = 2
  PacketListener packetListener = PacketListener.__new__(priority)
  PacketEvents.get().register_listener(packetListener)
  PacketEvents.__init__()

def onDisable():
  PacketEvents.get().terminate()
