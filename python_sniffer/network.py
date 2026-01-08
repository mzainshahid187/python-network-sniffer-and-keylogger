from scapy.all import sniff, Ether, IP, TCP, UDP, ICMP, ARP, IPv6
import datetime

def packet_callback(packet):
    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Start building the output string
    log_msg = f"[{timestamp}] "

    # Check for Ethernet Layer (Layer 2)
    if packet.haslayer(Ether):
        log_msg += f" {packet[Ether].src} -> {packet[Ether].dst} |"

    # Check for IP Layer (Layer 3)
    if packet.haslayer(IP):
        log_msg += f" IP {packet[IP].src} -> {packet[IP].dst} |"
    elif packet.haslayer(IPv6):
        log_msg += f" IPv6 {packet[IPv6].src} -> {packet[IPv6].dst} |"

    # Check for Protocol Layers (Layer 4)
    if packet.haslayer(TCP):
        log_msg += f" TCP Port: {packet[TCP].sport} -> {packet[TCP].dport}"
    elif packet.haslayer(UDP):
        log_msg += f" UDP Port: {packet[UDP].sport} -> {packet[UDP].dport}"
    elif packet.haslayer(ICMP):
        log_msg += f" ICMP Type: {packet[ICMP].type}"
    elif packet.haslayer(ARP):
        log_msg += f" ARP: {packet[ARP].psrc} is asking about {packet[ARP].pdst}"

    print(log_msg)

def main():
    print("--- Starting Scapy Sniffer ---")
    print("Press Ctrl+C to stop.")
    
    # sniff() arguments:
    # prn: function to run on each packet
    # store: 0 (don't keep packets in memory to prevent RAM bloat)
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
