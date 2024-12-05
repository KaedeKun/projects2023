from netmiko import ConnectHandler, NetMikoAuthenticationException
import pandas as pd
from pandas import ExcelWriter
from xlsxwriter import workbook, worksheet
import netaddr
from credenciales import user_without_radius, pass_without_radius
import pandas.io.formats.excel
pandas.io.formats.excel.ExcelFormatter.header_style = None

while True:
    direccion = input('Ingrese IP de router: ')
    if netaddr.valid_ipv4(direccion):
            break
    else:
        print("Ingrese direccion IP válida")
        continue

usuario = input('Ingrese usuario de logueo: ')
password = input('Ingrese password: ')

try:
    device_config = {
    "device_type": "huawei_vrpv8",
    "ip":direccion,
    "username":usuario,
    "password":password,
    "global_delay_factor": 10,
    }
    Connection = ConnectHandler(**device_config)
    device_name = Connection.find_prompt()[1:-1]
                    
except NetMikoAuthenticationException:
    device_config = {
    "device_type": "huawei_vrpv8",
    "ip":direccion,
    "username":usuario,
    "password":password,
    "global_delay_factor": 10,
    }
    Connection = ConnectHandler(**device_config)
    device_name = Connection.find_prompt()[1:-1]

#---------------------------------------------------------------------------------------------
#Obtener el nombre de maquina del equipo
# segment_sysname = Connection.send_command('display current-configuration | include sysname' )
# regex = (r'sysname\s+(.*)')
# match1 = json.dumps(re.findall(regex, segment_sysname))[2:-2]
# #---------------------------------------------------------------------------------------------

def write_file(archivo):
    with open(archivo,'w', encoding='utf-8') as escritura:
        resultado_alarmas=escritura.write('EQUIPO SIN ALARMAS')
        return resultado_alarmas
    
#COMANDOS REQUERIDOS PARA INVENTARIO ANTERIOR-ACTIVIDAD:
#
#VV display version                #VV display ospf peer brief
#VV display arp all                #VV display bfd session all
#VV dis current configuration      #VV display bgp vpnv4 all peer
#VV display interface brief        #VV display alarm active all
#VV dis ip interface brief
#VV dis lldp neighbor

screen                  = Connection.send_command("screen-length 0 temporary")
version                 = Connection.send_command("display version")
tabla_arp               = Connection.send_command("display arp all ")
interface_brief         = Connection.send_command("display interface brief")
config_actual           = Connection.send_command("display current-configuration")
interface_ip_brief      = Connection.send_command("display ip interface brief")
lldp_neighbors          = Connection.send_command("display lldp neighbor")
ospf_peer               = Connection.send_command("display ospf peer brief")
bfd_session             = Connection.send_command("display bfd session all")
bgp_peer                = Connection.send_command("display bgp vpnv4 all peer")
alarm_active            = Connection.send_command("display alarm active")
#---------------------------------------------------------------------------------------------
#Vuelta carnero (>_<) para asociar los nombres de archivo+ nombre host para ser procesados mas abajo
temp_texto_version = (f'temp_texto_version_{device_name}.txt')
temp_bgp_peer = (f'temp_bgp_peer_{device_name}.txt')
temp_tabla_arp = (f"temp_tabla_arp_{device_name}.txt")
temp_tabla_ip = (f'temp_tabla_ip_{device_name}.txt')
temp_configuracion_actual = (f'temp_configuracion_actual_{device_name}.txt')
temp_interface_brief = (f'temp_interface_brief_{device_name}.txt')
temp_lldp_neighbors = (f'temp_lldp_neighbors_{device_name}.txt')
temp_ospf_peers = (f'temp_ospf_peers_{device_name}.txt')
temp_bfd_sessions = (f'temp_bfd_sessions_{device_name}.txt')
temp_alarm_active = (f'temp_alarm_active_{device_name}.txt')
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#encoding para la salida de Netmiko para ser procesado por Pandas
with open(temp_bgp_peer, 'w', encoding='utf-8') as bgp_nei:
    final_bgp_peer = bgp_nei.write(bgp_peer)

with open(temp_texto_version,'w', encoding='utf-8') as v:
    final_version = v.write(version)

with open(temp_tabla_arp, 'w', encoding='utf-8') as arp:
    final_tabla_arp = arp.write(tabla_arp)

with open(temp_tabla_ip,'w', encoding='utf-8') as t:
    final_tabla_ip = t.write(interface_brief)

with open(temp_configuracion_actual, 'w', encoding='utf-8') as act_config:
    final_configuracion_actual = act_config.write(config_actual)

with open(temp_interface_brief, 'w', encoding='utf-8') as int_brief:
    final_interface_brief = int_brief.write(interface_ip_brief)

with open(temp_lldp_neighbors, 'w', encoding='utf-8') as lldp_nei:
    final_lldp_neighbors = lldp_nei.write(lldp_neighbors)

with open(temp_ospf_peers, 'w', encoding='utf-8') as ospf_nei:
    final_ospf_peer = ospf_nei.write(ospf_peer)   

with open(temp_bfd_sessions, 'w', encoding='utf-8') as bfd_sess:
    final_bfd_session = bfd_sess.write(bfd_session)

with open(temp_alarm_active, 'w', encoding='utf-8') as alarms:
    final_alarm_active = alarms.write(alarm_active)

with open(temp_alarm_active, 'r', encoding='utf-8') as read_alarms:
        char = read_alarms.read()
        if not char:
            write_file(temp_alarm_active)

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#Asignación de Dataframe para Pandas - read_table
df0 = pd.DataFrame(columns=['INTERFACE ORIGEN', 'INTERFACE DESTINO','DESCRIPCION','INTERFACE','TIPO','TIPO DE PUERTAS','Q NODOS'])
df1 = pd.read_table(temp_texto_version, on_bad_lines='skip')
df2 = pd.read_table(temp_tabla_arp, on_bad_lines='skip')
df3 = pd.read_table(temp_tabla_ip, on_bad_lines='skip')
df4 = pd.read_table(temp_configuracion_actual, on_bad_lines='skip')
df5 = pd.read_table(temp_interface_brief, on_bad_lines='skip')
df6 = pd.read_table(temp_lldp_neighbors, on_bad_lines='skip')
df7 = pd.read_table(temp_ospf_peers, on_bad_lines='skip')
df8 = pd.read_table(temp_bfd_sessions, on_bad_lines='skip')
df9 = pd.read_table(temp_bgp_peer, on_bad_lines='skip')
df10 = pd.read_table(temp_alarm_active, on_bad_lines='skip')
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#Asignacion de DataFrames a cada hoja del Excel + creacion de nombre de excel+nombre de host
router = (f"Inventario_{device_name}.xlsx")
writer = pd.ExcelWriter(router, engine='xlsxwriter')
df0.to_excel(writer, startcol=0, startrow=1, sheet_name='ORIGEN_DESTINO', index=False)
df1.to_excel(writer, startcol=0, startrow=1, sheet_name='VERSION', index=False)
df2.to_excel(writer, startcol=0, startrow=1, sheet_name='TABLA ARP', index=False)
df3.to_excel(writer, startcol=0, startrow=1, sheet_name='TABLA IP', index=False)
df4.to_excel(writer, startcol=0, startrow=1, sheet_name='CURRENT_CONFIG', index=False)
df5.to_excel(writer, startcol=0, startrow=1, sheet_name='INTERFACE_BRIEF', index=False)
df6.to_excel(writer, startcol=0, startrow=1, sheet_name='LLDP NEIGHBORS', index=False)
df7.to_excel(writer, startcol=0, startrow=2, sheet_name='OSPF PEERS', index=False)
df8.to_excel(writer, startcol=0, startrow=1, sheet_name='BFD SESSIONS', index=False)
df9.to_excel(writer, startcol=0, startrow=1, sheet_name='BGP PEERS', index=False)
df10.to_excel(writer, startcol=0, startrow=1, sheet_name='ALARMS', index=False)
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#Formateo de cada Sheet del Excel
workbook = writer.book
formato_fusion = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': 'yellow'})

def cel_formating(hoja):
    formato = workbook.add_format({'font_size':'10', 'align':'left', 'font_name':'Consolas'})
    final_formato = hoja.set_column('A:A', None, formato)

worksheet0 = writer.sheets['ORIGEN_DESTINO']
formato_00  = workbook.add_format({'font_size':'12', 'bold':1, 'align':'center','font_name':'Calibri'})
final_formato00 = worksheet0.set_column('A:A', None, formato_00)
final_fusion = worksheet0.merge_range('A1:G1', "SWAP EQUIPO "+device_name, formato_fusion)

worksheet1 = writer.sheets['VERSION']
cel_formating(worksheet1)
worksheet2 = writer.sheets['TABLA ARP']
cel_formating(worksheet2)
worksheet3 = writer.sheets['TABLA IP']
cel_formating(worksheet3)
worksheet4 = writer.sheets['CURRENT_CONFIG']
cel_formating(worksheet4)
worksheet5 = writer.sheets['INTERFACE_BRIEF']
cel_formating(worksheet5)
worksheet6 = writer.sheets['LLDP NEIGHBORS']
cel_formating(worksheet6)
worksheet7 = writer.sheets['OSPF PEERS']
cel_formating(worksheet7)
worksheet8 = writer.sheets['BFD SESSIONS']
cel_formating(worksheet8)
worksheet9 = writer.sheets['BGP PEERS']
cel_formating(worksheet9)
worksheet10 = writer.sheets['ALARMS']
cel_formating(worksheet10)
writer.close()
#---------------------------------------------------------------------------------------------
print('archivos generados.')