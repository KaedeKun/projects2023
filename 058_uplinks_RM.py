import textfsm
import json
import re
from colorama import Style,Fore
from netmiko import ConnectHandler, NetMikoAuthenticationException, NetMikoTimeoutException, NetmikoBaseException
from credenciales import user_radius, pass_radius, user_without_radius, pass_without_radius, soporte_pass, soporte_user
from concurrent.futures import ThreadPoolExecutor

equipos_core = {
"CX600-X16A-STG-P2" :ip1,
"CX6X8A-QUI-P2"     :ip2,
"CX600-X16A-STG-P1" :ip3,
"CX6X8A-QUI-P1"     :ip4,
}

#BGP PEER
def bgp_peer(conn_equipo):
    nombre_rr = []
    display_bgp_vpnv4_all_peer = conn_equipo.send_command(f'display bgp vpnv4 all peer')
    template_display_bgp_vpnv4_all_peer = open('templates\huawei_vrp_display_bgp_peer.textfsm')
    display_bgp_vpnv4_all_peer_table = textfsm.TextFSM(template_display_bgp_vpnv4_all_peer)
    fsm_result_display_bgp_vpnv4_all_peer= display_bgp_vpnv4_all_peer_table.ParseText(display_bgp_vpnv4_all_peer)
    for items in fsm_result_display_bgp_vpnv4_all_peer:
        for key, value in equipos_core.items():
            if str(value) == (items[0]):
                    nombre_rr.append(key)

    return nombre_rr

#EVPN PEER
def evpn_peer(conn_equipo):
    evpn_rr = []
    display_bgp_evpn_peer = conn_equipo.send_command(f'display bgp evpn peer')
    if len(display_bgp_evpn_peer) != 0:
        template_display_bgp_evpn_peer = open('templates\huawei_vrp_display_bgp_peer.textfsm')
        display_bgp_evpn_peer_table = textfsm.TextFSM(template_display_bgp_evpn_peer)
        fsm_result_display_bgp_evpn_peer = display_bgp_evpn_peer_table.ParseText(display_bgp_evpn_peer)
        for items in fsm_result_display_bgp_evpn_peer:
            for key, value in equipos_core.items():
                if str(value) == (items[0]):
                    evpn_rr.append(key)
    else:
        return None    
    
    return evpn_rr

#LLDP NEIGHBOR BRIEF 
def lldp_nei_brief(conn_equipo):
    display_lldp_neighbro_brief = conn_equipo.send_command(f'display lldp neighbor brief')
    template_display_lldp_nei_brief = open('templates\huawei_vrp_display_lldp_neighbor_brief.textfsm')
    display_lldp_nei_brief_table = textfsm.TextFSM(template_display_lldp_nei_brief)
    fsm_result_display_lldp_nei_brief = display_lldp_nei_brief_table.ParseText(display_lldp_neighbro_brief)

    return fsm_result_display_lldp_nei_brief

def confirmation_uplink(conn_equipo, troncales):
    display_interface_troncal = conn_equipo.send_command(f"display interface {troncales}")
    if bool(re.search("Wrong",display_interface_troncal)) == False:
            template_display_interface_troncal = open('templates\huawei_vrp_display_interface.textfsm')
            display_interface_troncal_table = textfsm.TextFSM(template_display_interface_troncal)
            fsm_result_display_interface_troncal = display_interface_troncal_table.ParseText(display_interface_troncal)

    else:
        return 0
        
    return fsm_result_display_interface_troncal

def llamada_a_equipos(device):
        try:
            device_config = {
            "device_type": "huawei_vrpv8",
            "ip":device,
            "username":user_radius,
            "password":pass_radius,       
            "global_delay_factor": .5,
            }
            Connection = ConnectHandler(**device_config)
            device_name = Connection.find_prompt()
                        
        except NetMikoAuthenticationException:
                device_config = {
                "device_type": "huawei_vrpv8",
                "ip":device,
                "username":user_without_radius,
                "password":pass_without_radius,
                "global_delay_factor": .5,
                }
                Connection = ConnectHandler(**device_config)
                device_name = Connection.find_prompt()

        bgp_list = bgp_peer(Connection)
        evpn_list = evpn_peer(Connection)
        if evpn_list !=None:
            evpn_list.sort()
        else:
            evpn_list = ""
        bgp_list.sort()
        if (len(bgp_list) and len(evpn_list)!=0):
            if bgp_list == evpn_list:
                print(f"{device_name},\t BGP & EVPN IGUALES")
            else:
                print(f"{device_name},\t BGP & EVPN NO IGUALES")
        else:
            print(f"{device_name},\t NO EVPN Peers")

        troncales = ["Eth-Trunk10","Eth-Trunk15","Eth-Trunk30"]
        for items in troncales:
                result_confirmacion_uplink = confirmation_uplink(Connection,items)
                if result_confirmacion_uplink !=0:
                    for qq in result_confirmacion_uplink:
                        for ll in lldp_nei_brief(Connection):
                            lldp_uplink = ll[1]
                            lldp_interface = ll[0]
                            if qq[0] == lldp_interface:
                                for key, value in equipos_core.items():
                                    if key == lldp_uplink:
                                        print(f"{device_name},\t {lldp_uplink}, {items}")


with open('listado_rms.txt', 'r') as equipos:
    device_list = equipos.read().splitlines()

with ThreadPoolExecutor(max_workers=5) as executor:
    for device in device_list:
        try:
            future = executor.submit(llamada_a_equipos, device)
        except Exception as e:
            print(f'error al enviar la Tarea al Thread: {e}')