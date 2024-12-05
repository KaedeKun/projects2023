## ACA VIVEN LOS TEXTFSM DE CADA PEER
## ['Internacional_v4', 'Internacional_v6', 'Nacional_v4', 'Peering_v4', 'PIT-Chile_v4', 'CDN_v4', 'ASN']
from netmiko import ConnectHandler
from credenciales import soporte_user, soporte_pass
import textfsm

device_IGR_RSS = {
    "device_type": "huawei_vrpv8",
    "ip": ip,
    "username":soporte_user,
    "password":soporte_pass,
    "global_delay_factor": .2,
}
Connection_RSS = ConnectHandler(**device_IGR_RSS)

device_IGR_QUI = {
    "device_type": "huawei_vrpv8",
    "ip": "10.50.1.52",
    "username":soporte_user,
    "password":soporte_pass,
    "global_delay_factor": .2,
}
Connection_QUI = ConnectHandler(**device_IGR_QUI)

#--------------------------------INTERNACIONAL_V4--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------

def int_parser_bgp_routing_v4_stg_lumen():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 8.243.191.89 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def int_parser_bgp_routing_v4_qui_lumen():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 8.243.191.85 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def int_parser_bgp_routing_v4_stg_ixmetro():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 198.18.204.61 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def int_parser_bgp_routing_v4_qui_ixmetro():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 198.18.204.37 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def int_parser_bgp_routing_v4_stg_telefonica():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 186.148.20.45 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def int_parser_bgp_routing_v4_qui_telefonica():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 186.148.24.37 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def int_parser_bgp_routing_v4_stg_claro():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 172.18.7.173 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def int_parser_bgp_routing_v4_qui_claro():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 172.18.7.185 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def int_parser_bgp_routing_v4_stg_cogent():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 199.100.16.225 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def int_parser_bgp_routing_v4_qui_cogent():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 199.100.16.233 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count


#--------------------------------INTERNACIONAL_V6--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------ STG LUMEN V6---------------------------------------------------------------------------------------
def int_v6_parser_bgp_routing_stg_lumen():
		display_bgp_routing_v6 = Connection_RSS.send_command(f'display bgp ipv6 routing-table peer 2001:13B0:4000:1A::1 advertised-routes')
		if len(display_bgp_routing_v6) != 0:
			template_bgp_routing_v6 = open('templates\huawei_vrp_display_bgp_ipv6_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v6_table = textfsm.TextFSM(template_bgp_routing_v6)
			fsm_result_bgp_routing_v6 = bgp_routing_v6_table.ParseText(display_bgp_routing_v6)
			for count, line in enumerate(fsm_result_bgp_routing_v6):
				pass
				count+1
		else:
			fsm_result_bgp_routing_v6  = 0
			count = 0
					
		return fsm_result_bgp_routing_v6, count
		
#------------------------------------ QUI LUMEN V6---------------------------------------------------------------------------------------
def int_v6_parser_bgp_routing_qui_lumen():
		display_bgp_routing_v6 = Connection_QUI.send_command(f'display bgp ipv6 routing-table peer 2001:13B0:4000:19::1 advertised-routes')
		if len(display_bgp_routing_v6) != 0:
			template_bgp_routing_v6 = open('templates\huawei_vrp_display_bgp_ipv6_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v6_table = textfsm.TextFSM(template_bgp_routing_v6)
			fsm_result_bgp_routing_v6 = bgp_routing_v6_table.ParseText(display_bgp_routing_v6)
			for count, line in enumerate(fsm_result_bgp_routing_v6):
				pass
				count+1
		else:
			fsm_result_bgp_routing_v6  = 0
			count = 0
					
		return fsm_result_bgp_routing_v6, count

#------------------------------------ STG IXMETRO V6---------------------------------------------------------------------------------------
def int_v6_parser_bgp_routing_stg_ixmetro():
		display_bgp_routing_v6 = Connection_RSS.send_command(f'display bgp ipv6 routing-table peer 2803:8180:1::ED advertised-routes')
		if len(display_bgp_routing_v6) != 0:
			template_bgp_routing_v6 = open('templates\huawei_vrp_display_bgp_ipv6_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v6_table = textfsm.TextFSM(template_bgp_routing_v6)
			fsm_result_bgp_routing_v6 = bgp_routing_v6_table.ParseText(display_bgp_routing_v6)
			for count, line in enumerate(fsm_result_bgp_routing_v6):
				pass
				count+1
		else:
			fsm_result_bgp_routing_v6  = 0
			count = 0
					
		return fsm_result_bgp_routing_v6, count

#------------------------------------ QUI IXMETRO V6---------------------------------------------------------------------------------------
def int_v6_parser_bgp_routing_qui_ixmetro():
		display_bgp_routing_v6 = Connection_QUI.send_command(f'display bgp ipv6 routing-table peer 2803:8180:1::D9 advertised-routes')
		if len(display_bgp_routing_v6) != 0:
			template_bgp_routing_v6 = open('templates\huawei_vrp_display_bgp_ipv6_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v6_table = textfsm.TextFSM(template_bgp_routing_v6)
			fsm_result_bgp_routing_v6 = bgp_routing_v6_table.ParseText(display_bgp_routing_v6)
			for count, line in enumerate(fsm_result_bgp_routing_v6):
				pass
				count+1
		else:
			fsm_result_bgp_routing_v6  = 0
			count = 0
					
		return fsm_result_bgp_routing_v6, count

#------------------------------------ STG TELEFONICA V6---------------------------------------------------------------------------------------
def int_v6_parser_bgp_routing_stg_telefonica():
		display_bgp_routing_v6 = Connection_RSS.send_command(f'display bgp ipv6 routing-table peer 2800:550:6:11C::1 advertised-routes')
		if len(display_bgp_routing_v6) != 0:
			template_bgp_routing_v6 = open('templates\huawei_vrp_display_bgp_ipv6_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v6_table = textfsm.TextFSM(template_bgp_routing_v6)
			fsm_result_bgp_routing_v6 = bgp_routing_v6_table.ParseText(display_bgp_routing_v6)
			for count, line in enumerate(fsm_result_bgp_routing_v6):
				pass
				count+1
		else:
				fsm_result_bgp_routing_v6  = 0
				count = 0
					
		return fsm_result_bgp_routing_v6, count

#------------------------------------ QUI TELEFONICA V6---------------------------------------------------------------------------------------
def int_v6_parser_bgp_routing_qui_telefonica():
		display_bgp_routing_v6 = Connection_QUI.send_command(f'display bgp ipv6 routing-table peer 2800:550:88::1 advertised-routes')
		if len(display_bgp_routing_v6) != 0:
			template_bgp_routing_v6 = open('templates\huawei_vrp_display_bgp_ipv6_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v6_table = textfsm.TextFSM(template_bgp_routing_v6)
			fsm_result_bgp_routing_v6 = bgp_routing_v6_table.ParseText(display_bgp_routing_v6)
			for count, line in enumerate(fsm_result_bgp_routing_v6):
				pass
				count+1
		else:
				fsm_result_bgp_routing_v6  = 0
				count = 0
					
		return fsm_result_bgp_routing_v6, count

#------------------------------------ STG COGENT V6---------------------------------------------------------------------------------------
def int_v6_parser_bgp_routing_stg_cogent():
		display_bgp_routing_v6 = Connection_RSS.send_command(f'display bgp ipv6 routing-table peer 2804:5330:2:3::1C:1 advertised-routes')
		if len(display_bgp_routing_v6) != 0:
			template_bgp_routing_v6 = open('templates\huawei_vrp_display_bgp_ipv6_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v6_table = textfsm.TextFSM(template_bgp_routing_v6)
			fsm_result_bgp_routing_v6 = bgp_routing_v6_table.ParseText(display_bgp_routing_v6)
			for count, line in enumerate(fsm_result_bgp_routing_v6):
				pass
				count+1
		else:
				fsm_result_bgp_routing_v6  = 0
				count = 0
					
		return fsm_result_bgp_routing_v6, count

#------------------------------------ QUI COGENT V6---------------------------------------------------------------------------------------
def int_v6_parser_bgp_routing_qui_cogent():
		display_bgp_routing_v6 = Connection_QUI.send_command(f'display bgp ipv6 routing-table peer 2804:5330:2:3::1D:1 advertised-routes')
		if len(display_bgp_routing_v6) != 0:
			template_bgp_routing_v6 = open('templates\huawei_vrp_display_bgp_ipv6_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v6_table = textfsm.TextFSM(template_bgp_routing_v6)
			fsm_result_bgp_routing_v6 = bgp_routing_v6_table.ParseText(display_bgp_routing_v6)
			for count, line in enumerate(fsm_result_bgp_routing_v6):
				pass
				count+1
		else:
				fsm_result_bgp_routing_v6  = 0
				count = 0
					
		return fsm_result_bgp_routing_v6, count

#-------------------------------------NACIONAL_V4--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------

def nac_parser_bgp_routing_v4_stg_lumen():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 190.217.41.109 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
				pass
				count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def nac_parser_bgp_routing_v4_qui_lumen():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 190.217.41.105 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def nac_parser_bgp_routing_v4_stg_ixmetro():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 198.18.204.57 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def nac_parser_bgp_routing_v4_qui_ixmetro():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 198.18.204.33 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def nac_parser_bgp_routing_v4_stg_telefonica():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 186.148.20.41 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def nac_parser_bgp_routing_v4_qui_telefonica():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 186.148.24.33 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def nac_parser_bgp_routing_v4_stg_claro():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 172.18.7.61 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def nac_parser_bgp_routing_v4_qui_claro():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 192.168.169.205 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

#-------------------------------------PEERING _V4--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------
def peering_parser_bgp_routing_v4_stg_akamai():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 190.107.230.127 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def peering_parser_bgp_routing_v4_qui_akamai():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 201.219.232.127 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def peering_parser_bgp_routing_v4_stg_google():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 72.14.222.54 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def peering_parser_bgp_routing_v4_qui_google():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 209.85.173.82 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def peering_parser_bgp_routing_v4_stg_facebook():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 157.240.82.204 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def peering_parser_bgp_routing_v4_qui_facebook():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 157.240.74.216 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def peering_parser_bgp_routing_v4_stg_microsoft():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 104.44.197.41 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def peering_parser_bgp_routing_v4_qui_microsoft():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 104.44.197.39 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def peering_parser_bgp_routing_v4_stg_amazon():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 99.83.94.130 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def peering_parser_bgp_routing_v4_qui_amazon():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 99.83.94.128 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def peering_parser_bgp_routing_v4_stg_stackpath():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 99.83.94.130 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def peering_parser_bgp_routing_v4_stg_twitch():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 99.181.103.82 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def peering_parser_bgp_routing_v4_qui_twitch():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 99.181.103.84 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

#-------------------------------------PIT CHILE V4-------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------
def pitchile_parser_bgp_routing_v4_stg_pitchile1():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 45.68.16.1 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def pitchile_parser_bgp_routing_v4_stg_pitchile2():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 45.68.16.2 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def pitchile_parser_bgp_routing_v4_qui_pitchile1():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 45.68.16.1 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def pitchile_parser_bgp_routing_v4_qui_pitchile2():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 45.68.16.2 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def pitchile_parser_bgp_routing_v4_stg_i3D():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 45.68.16.144 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def pitchile_parser_bgp_routing_v4_qui_i3D():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 45.68.16.144 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def pitchile_parser_bgp_routing_v4_stg_riotgames1():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 45.68.16.185 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def pitchile_parser_bgp_routing_v4_stg_riotgames2():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 45.68.16.186 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def pitchile_parser_bgp_routing_v4_qui_riotgames1():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 45.68.16.185 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def pitchile_parser_bgp_routing_v4_stg_EdgeUno1():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 45.68.16.79 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def pitchile_parser_bgp_routing_v4_stg_EdgeUno2():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 45.68.16.189 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def pitchile_parser_bgp_routing_v4_qui_EdgeUno1():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 45.68.16.79 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def pitchile_parser_bgp_routing_v4_qui_EdgeUno2():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 45.68.16.189 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def pitchile_parser_bgp_routing_v4_stg_ATT():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 45.68.16.188 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def pitchile_parser_bgp_routing_v4_qui_ATT():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 45.68.16.188 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def pitchile_parser_bgp_routing_v4_stg_valve1():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 45.68.16.190 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def pitchile_parser_bgp_routing_v4_stg_valve2():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 45.68.16.191 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def pitchile_parser_bgp_routing_v4_qui_valve1():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 45.68.16.190 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def pitchile_parser_bgp_routing_v4_qui_valve2():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 45.68.16.191 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def pitchile_parser_bgp_routing_v4_stg_fastly1():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 45.68.16.200 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def pitchile_parser_bgp_routing_v4_stg_fastly2():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 45.68.16.201 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def pitchile_parser_bgp_routing_v4_qui_fastly1():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 45.68.16.200 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def pitchile_parser_bgp_routing_v4_qui_fastly2():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 45.68.16.201 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def pitchile_parser_bgp_routing_v4_stg_cloudflare():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 45.68.16.227 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def pitchile_parser_bgp_routing_v4_qui_cloudflare():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 45.68.16.227 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def pitchile_parser_bgp_routing_v4_stg_verisign():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 45.68.16.230 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def pitchile_parser_bgp_routing_v4_qui_verisign():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 45.68.16.230 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def pitchile_parser_bgp_routing_v4_stg_gcorelab():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 45.68.16.239 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def pitchile_parser_bgp_routing_v4_qui_gcorelab():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 45.68.16.239 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

#-------------------------------------CDNs V4-------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------
def cdn_parser_bgp_routing_v4_stg_google():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 45.232.33.94 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def cdn_parser_bgp_routing_v4_qui_google():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 168.196.202.97 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def cdn_parser_bgp_routing_v4_stg_netflix():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 190.107.230.11 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count


def cdn_parser_bgp_routing_v4_qui_netflix():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 186.189.84.22 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def cdn_parser_bgp_routing_v4_stg_facebook():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 201.219.232.144 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count


def cdn_parser_bgp_routing_v4_qui_facebook():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 45.232.35.80 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def cdn_parser_bgp_routing_v4_stg_tiktok():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 186.189.84.3 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count


def cdn_parser_bgp_routing_v4_qui_tiktok():
		display_bgp_routing_v4 = Connection_QUI.send_command(f'display bgp routing-table peer 186.189.84.5 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def cdn_parser_bgp_routing_v4_stg_apple():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 168.196.200.121 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def cdn_parser_bgp_routing_v4_stg_cdn77():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 186.189.84.153 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
			template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
			bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
			fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
			for count, line in enumerate(fsm_result_bgp_routing_v4):
					pass
					count+1
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
			
		return fsm_result_bgp_routing_v4, count

def cdn_parser_bgp_routing_v4_stg_cloudflare():
		display_bgp_routing_v4 = Connection_RSS.send_command(f'display bgp routing-table peer 45.232.33.129 advertised-routes')
		if len(display_bgp_routing_v4) != 0:
				if not "A default" in display_bgp_routing_v4:
					template_bgp_routing_v4 = open('templates\huawei_vrp_display_bgp_routing_table_peer_ip_advertised-routes.textfsm')
					bgp_routing_v4_table = textfsm.TextFSM(template_bgp_routing_v4)
					fsm_result_bgp_routing_v4 = bgp_routing_v4_table.ParseText(display_bgp_routing_v4)
					for count, line in enumerate(fsm_result_bgp_routing_v4):
						pass
						count+1
				else:
					fsm_result_bgp_routing_v4  = 0
					count = 0
		else:
			fsm_result_bgp_routing_v4  = 0
			count = 0
				
		return fsm_result_bgp_routing_v4, count
