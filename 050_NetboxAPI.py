import pynetbox
from netmiko import ConnectHandler
import json
import re
import textfsm
import requests
from colorama import Fore
from credenciales import NB_API_TOKEN, NB_URL,user_radius, pass_radius, user_without_radius, pass_without_radius

## SINTAXIS DE VELOCIDADES:
## 1Gb  SFP = 1000base-x-sfp
## 10Gb SFP+ = 10gbase-x-sfpp
## 1Gb Ethernet = 1000base-t

HEADERS = {'Authorization': f'Token {NB_API_TOKEN}',
            'Content-Type': 'application/json', 'Accept': 'application/json'}

device_config = {
    "device_type": "huawei_vrpv8",
    "ip":ip_addr,
    #"ip": "10.50.1.155",
    #"username":user_radius,
    #"password":pass_radius,
    #"username":user_without_radius,
    "global_delay_factor": .5
}
Connection = ConnectHandler(**device_config)

# -----------------------OBTENIENDO EL NOMBRE DE HOST-----------------------
# -----------------------OBTENIENDO EL MODELO DEL HOST----------------------

segment_sysname = Connection.send_command('display current-configuration | include sysname' )
regex = (r'sysname\s+(.*)')
device_name = json.dumps(re.findall(regex, segment_sysname))[2:-2]
# --------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  OBTENER EL MODELO Y LA SERIE DEL EQUIPO (ESN)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# display_version = Connection.send_command('display version')
# template_version = open('templates\huawei_vrp_display_version.textfsm')

# display_version_table = textfsm.TextFSM(template_version)
# fsm_result_version = display_version_table.ParseText(display_version)

# for uu in fsm_result_version:
#     device_modelo = uu[2]
#     if device_modelo == 'ATN 910C-G':
#         modeling = 1
#     elif device_modelo == 'ATN 950C':
#         modeling = 3
#     elif device_modelo == 'CX600-X2-M8':
#         modeling = 4
#     else:
#         modeling = 2

modeling = 2
display_esn = Connection.send_command('display esn')

regex_esn = (r'ESN of master:+(.*)')
device_serial = json.dumps(re.findall(regex_esn, display_esn))[2:-2]

#------------------------VERIFICAR SI EXISTE EL EQUIPO---------------------
#--------------------------------------------------------------------------
def already_exist(device_name):
    request_url = f"{NB_URL}/api/dcim/devices/?q={device_name}"
    si_existe = requests.get(request_url, headers=HEADERS)
    result_count = si_existe.json()
    #print(result)
    count = result_count["count"]
    return count

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
display_interface_description = Connection.send_command('display interface description')
template_interface_description = open('templates\huawei_vrp_display_interface_description.textfsm')

interface_description_table = textfsm.TextFSM(template_interface_description)
fsm_result = interface_description_table.ParseText(display_interface_description)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

display_ip_interface_brief = Connection.send_command('display ip interface brief')
template_ip_interface_brief  = open('templates\huawei_vrp_display_ip_interface_brief.textfsm')

ip_interface_brief_table = textfsm.TextFSM(template_ip_interface_brief)
fsm_result_3 = ip_interface_brief_table.ParseText(display_ip_interface_brief)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

display_arp_all = Connection.send_command('display arp all')
template_arp_all = open('templates\huawei_vrp_display_arp_all.textfsm')

display_arp_all_table = textfsm.TextFSM(template_arp_all)
fsm_result_4 = display_arp_all_table.ParseText(display_arp_all)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#----------------------------------------------------------------------------------

# OBTENER IP DEL COMANDO display interface brief (para futuras referencias)
# lista_ip = []
# lista = []
# for j in fsm_result_3:
#     lista_ip.append(j[1])
#     while(lista_ip.count("unassigned")):
#             lista_ip.remove("unassigned")

# for jj in lista_ip:
#     add_ipprefix_global_ip(jj)
#----------------------------------------------------------------------------------
nb = pynetbox.api(NB_URL, threading= True, token=NB_API_TOKEN)

def updating_device(dev, serial, modelo):
        update_device = nb.dcim.devices.get(name=device_name)
        update_device.device_type=modelo
        update_device.device_role=1
        update_device.site=1
        update_device.serial=serial
        update_device.save()

def create_device(dev, serial, modeling):
        result = nb.dcim.devices.create( 
        name=device_name,
        device_type=modeling,
        device_role=1,
        site=1,
        serial=serial,
        )

        print('El equipo ingresado es: '+ str(result))

if (already_exist(device_name) == 0):
    print('Agregando equipo...............')
    create_device(device_name, device_serial, modeling)
else: 
    print(f"El equipo {device_name} ya existe en el inventario!, actualizando.....")
    print(f'Actualizando los datos de {device_name.upper()}')
    updating_device(device_name, device_serial, modeling)

#except pynetbox.core.query.RequestError:
#----------------------------------------------------------------------------------       
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
# ID DEL DISPOSITIVO ( DEVICE NAME)
def request_devices(device_name):
    request_url = f"{NB_URL}/api/dcim/devices/?q={device_name}"
    devices = requests.get(request_url, headers=HEADERS)
    result = devices.json()
    #print(result)
    id = result["results"][0]["id"]
    return id

#print('el dispositivo tiene el ID: '+ str(request_devices(device_name)))
#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#ID DE LA INTERFAZ (DEVICE INTERFACE)
# def request_interface(filtro_interface):
#      interface_id = nb.dcim.interfaces.get(name=filtro_interface, device=device_name).id
#      return interface_id

def request_interface(filtro_interface):
    request_url = f"{NB_URL}/api/dcim/interfaces/?name={filtro_interface}"
    url_interface = requests.get(request_url, headers=HEADERS)
    result_interface = url_interface.json()
    for valores_int in result_interface["results"]:
            if valores_int["device"]["name"] == device_name:
                return valores_int['id']
            
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
def request_id_ip_address(ip_address_name):
    id_device = request_devices(device_name)
    dir_ip = nb.ipam.ip_addresses.get(address=ip_address_name)
    if (dir_ip.assigned_object.device.id == id_device):
         direccion_ip_id = dir_ip.id
         return direccion_ip_id
         
# #ID DE LA IP (DEVICE IP ADDRESS)
# def request_id_ip_address(ip_address_name, device_name):
#     device_name = device_name
#     request_url = f"{NB_URL}/api/ipam/ip-addresses/?address={ip_address_name}"
#     url_ip = requests.get(request_url, headers=HEADERS)
#     result_ip = url_ip.json()
#     for valores_ip in (result_ip["results"]):
#             if valores_ip ["assigned_object"]["device"]["name"] == device_name:
#                 return valores_ip['id']

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#ID DE VRF
def request_vrf(name_vrf):
        request_vrf = f"{NB_URL}/api/ipam/vrfs/?name={name_vrf}"
        url_vrf = requests.get(request_vrf, headers=HEADERS)
        result_interface = url_vrf.json()
        for valores_vrf in result_interface["results"]:
            return valores_vrf['id']
        

#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------

def updating_interfaces(device_name, nombre_interface, nombre_description, estatus, tipo_int, inter_vrf):
    identificador  = request_devices(device_name)
    name_int = request_interface(nombre_interface)
    update_device_interface = nb.dcim.interfaces.get(name=nombre_interface, device=device_name)
    name_status = estatus
    update_device_interface.name=nombre_interface
    update_device_interface.description=nombre_description
    update_device_interface.type=tipo_int
    update_device_interface.enabled=name_status
    update_device_interface.vrf=inter_vrf
    update_device_interface.save()
    print(f"Agregando información de la interfaz : {nombre_interface} al equipo : {device_name} con VRF: {inter_vrf}")

def post_interfaces(device_name,nombre_interface,nombre_description, estatus, type, int_vrf):
    id  = request_devices(device_name)
    request_url = f"{NB_URL}/api/dcim/interfaces/?device={device_name}"
    interface_parameters = {
        "device": id,
        "name": nombre_interface,
        "description": nombre_description,
        "type": type,
        "enabled": estatus,
        "vrf": int_vrf,
    }
    new_interfaces = requests.post(
        request_url, headers=HEADERS, json=interface_parameters)
    print(f'Agregado {nombre_interface} al equipo: {device_name.upper()}, con VRF: {int_vrf}')


#fsm_result = display interface description
contador_fsm_result = 0
for ii in fsm_result:
    nombre_interface = ii[0]
    nombre_description = ii[3]
    if ii[1] == "down":
        estatus = "False"
    else:
        estatus = "True"

    if bool(re.search(r"(10G)", nombre_interface)) == True:
        nombre_interface = nombre_interface[:-5]
        type = "10gbase-x-sfpp"
        
    elif bool(re.search(r"(100M)", nombre_interface)) == True:
        nombre_interface = nombre_interface[:-6]
        type = '100base-tx'
    
    elif bool(re.search(r"(Eth0/0/0)", nombre_interface)) == True:
         type = '100base-tx'
    else:
        type = "1000base-x-sfp"
    
    if bool(re.search(r"Eth-Trunk|Loop", nombre_interface)) == True:
        type = "virtual"

    if  bool(re.search((r'O&M'), nombre_description)) == True:
        vrf_name = 2
    elif  bool(re.search((r"TR069"), nombre_description)) == True:
        vrf_name = 6
    elif  bool(re.search((r"WOMTV"), nombre_description)) == True:
        vrf_name = 8
    elif  bool(re.search((r"VOIP"), nombre_description)) == True:
         vrf_name = 5
    elif  bool(re.search((r"Iu_B"), nombre_description)) == True:
         vrf_name = 3
    elif  bool(re.search((r"s1"), nombre_description)) == True:  
         vrf_name = 1
    elif  bool(re.search((r"tiendas"), nombre_description)) == True:
        vrf_name = 7
    elif bool(re.search(r"(Loop1)", nombre_interface)) == True:
         vrf_name = 2
    else:
        vrf_name = 4
    if already_exist(device_name) == 0:
        post_interfaces(device_name, nombre_interface, nombre_description, estatus, type,vrf_name)
    else:
        post_interfaces(device_name, nombre_interface, nombre_description, estatus, type,vrf_name)
        updating_interfaces(device_name, nombre_interface, nombre_description,estatus, type,vrf_name)
        
    contador_fsm_result+=1

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------
# AGREGAR LAS IP ASOCIADAS A SU RESPECTIVA VRF-INSTANCE (INCLUSO LAS DOWN)

def updating_ipprefix_global(prefix_ip, prefix_vrf, interface):
    #IP / INTERFACE OBTENIDA DEL ROUTER
    inco_ip_address = prefix_ip+"/32"
    inco_interface = interface
    #IP OBTENIDA DE NETBOX (EN BASE A LO RECIBIDO, A VER SI EXISTE EN NETBOX)
    incoming_ip_interface = nb.ipam.ip_addresses.get(address=inco_ip_address)
    # OBTENER ID DE LA INTERFAZ  ( EN BASE A LO RECIBIDO, A VER SI EXISTE EN NETBOX)
    incoming_interface_id = nb.dcim.interfaces.get(device=device_name, name=inco_interface).id
    #DICCIONARIO CON LOS DATOS OBTENIDOS DEL ROUTER
    #ADDRESS DIRECCION OBTENIDA DEL ROUTER
    #ASSIGNED OBJECT ID, ID INTERFAZ EN BASE A LO RECIBIDO POR EL ROUTER ( A VER SI EXISTE EN NETBOX)
    #ASSIGNED OBJECT TYPE, VALOR FIJO ASOCIADO A LA IP PARA ASIGNACION DE INTERFACE
    incoming_data = dict (
        address = inco_ip_address,
        assigned_object_id = incoming_interface_id,
        assigned_object_type="dcim.interface",
    )
    #SI LA IP OBTENIDA DEL ROUTER, NO EXISTE, ENTONCES CREALA Y ASOCIALA AL ID DE LA INTERFAZ EN LA QUE ESTA ASOCIADA EN BASE A LO RECIBIDO POR EL ROUTER
    if nb.ipam.ip_addresses.get(q=inco_ip_address) == None:
        incoming = nb.ipam.ip_addresses.create(address=inco_ip_address)
        incoming.vrf = prefix_vrf
        incoming.assigned_object_type = "dcim.interface"
        incoming.assigned_object_id = nb.dcim.interfaces.get(device=device_name, name=inco_interface).id
        incoming.save()
    else:
        #EN CASO DE QUE EXISTE, ENTONCES ACTUALIZA LOS VALORES CON EL DICCIONARIO ANTERIORMENTE DEFINIDO
        incoming_ip_interface.update(incoming_data)


    if incoming_ip_interface.assigned_object_id != incoming_interface_id:
        incoming_ip_interface.update(incoming_data)

    # incoming_ip_interface = nb.ipam.ip_addresses.get(address=incoming_ip_address)
    # net_ip_interface = nb.ipam.ip_addresses.get(address=incoming_ip_address)
    # if nb.ipam.ip_addresses.get(address=incoming_ip_address) == None:

    #         print("Agregación de IP")
    # else:
    #     pass
    
    # if incoming_ip_interface.assigned_object_id != net_ip_interface.assigned_object_id:
    #         net_ip_interface.assigned_object_type.delete()
    #         net_ip_interface.assigned_object_id.delete()
    # else:
    #         nb.ipam.ip_addresses.get(address=incoming_ip_address).assigned_object_type = "dcim.interface"
    #         nb.ipam.ip_addresses.get(address=incoming_ip_address).assigned_object_id = nb.dcim.interfaces.get(device=device_name, name=incoming_interface).id
    #         incoming_ip_interface.save()

    # # #if str(nb.ipam.ip_addresses.get(address=new_ip_address)) == new_ip_address:
        
    # # ip_obj = nb.ipam.ip_addresses.get(address=ip_address)
    # # interface_obj = nb.dcim.interfaces.get(device=device_name, name=interface_name)
    # # if ip_obj.address == ip_address:
    # # #if ip_obj.assigned_object.id == interface_obj.id:
    # #     pass
    # # else:
    # #     ip_obj.assigned_object.id = interface_obj.id
    # #     ip_obj.display = ip_address
    # #     ip_obj.address = ip_address
    # #     ip_obj.vrf = prefix_vrp
    #     # ip_obj.save()
    # # else:
    # #     ip_obj.delete()
    # #ip_obj.assigned_object.id != interface_obj.id:



def add_ipprefix_global(prefix_ip, prefix_vrf, interface):
    #id  = request_devices(device_name)
    request_url = f"{NB_URL}/api/ipam/ip-addresses/"
    ip_address_vrf = {
        "display": prefix_ip,
        "address": prefix_ip,
        "vrf": prefix_vrf,
        "assigned_object_type": "dcim.interface",
        "assigned_object_id": interface,
    }
    if prefix_vrf == 1:
         nom_vrf = "S1"
    elif prefix_vrf == 2:
         nom_vrf = "O&M"
    elif prefix_vrf == 3:
         nom_vrf = "Iu_B"
    elif prefix_vrf == 7:
         nom_vrf = "Tiendas"
    elif prefix_vrf == 8:
         nom_vrf = "womtv"
    elif prefix_vrf == 5:
         nom_vrf = "Gi_Swu"
    elif prefix_vrf == 6:
         nom_vrf = "fttx_tr069"
    else:
        nom_vrf = "Global"
    new_prefix_global = requests.post(
        request_url, headers=HEADERS, json=ip_address_vrf)
    print("con vpn-instance :"+str(nom_vrf), "se agregó el segmento: "+str(prefix_ip), "asociada a la interface :"+str(interface))


#fsm_result_4 = display arp all
vrf_instance = 0
for hr in fsm_result_4:
    filtro_interface = hr[4]
    filtro_ip = hr[0]
    vrf_direccion = hr[5]
    filtro_vlan = hr[3]
    # if filtro_interface == 'GE0/6/0':
    #     filtro_interface = 'GE0/6/0(100M)'
    if filtro_vlan == 'I -':
            #print(filtro_interface, filtro_ip, vrf_direccion)
            if bool(re.search(r"s1", vrf_direccion)) == True:
                    vrf_instance = 1
            elif bool(re.search(r"O&M", vrf_direccion)) == True:
                    vrf_instance = 2
            elif bool(re.search(r"Iu_B", vrf_direccion)) == True:
                    vrf_instance = 3
            elif bool(re.search(r"tiendas", vrf_direccion)) == True:
                    vrf_instance = 7
            elif bool(re.search(r"womtv", vrf_direccion)) == True:
                    vrf_instance = 8
            elif bool(re.search(r"Gi_Swu", vrf_direccion)) == True:
                    vrf_instance = 5
            elif bool(re.search(r"fttx_tr069", vrf_direccion)) == True:
                    vrf_instance = 6
            else:
                    vrf_instance = 4
            if already_exist(device_name) == 0:
                add_ipprefix_global(filtro_ip,vrf_instance,request_interface(filtro_interface))

            else:
                print('actualizando IPs')
                #add_ipprefix_global(filtro_ip,vrf_instance,request_interface(filtro_interface))
                updating_ipprefix_global(filtro_ip, vrf_instance, filtro_interface)


#----------------------------------------------------------------------------------
# AGREGAR SOLO LAS INTERFACES LOOPBACKS  TAMBIEN SUS INTERFACES ASOCIADAS (LOOP0 /LOOP1)
def add_vrf_loopback(loopback_ip, loopback_vrf, ip_primary):
    #id_device  = request_devices(device_name)
    request_url = f"{NB_URL}/api/ipam/ip-addresses/"
    ip_address_loopback = {
       "address": loopback_ip,
       "vrf": loopback_vrf,
        "assigned_object_type": "dcim.interface",
        "assigned_object_id": ip_primary,
    }
    if loopback_vrf == 2:
        loop_vrf = "O&M"
    else:
        loop_vrf = "Global"
    new_vrf_loopbacks = requests.post(
        request_url, headers=HEADERS, json=ip_address_loopback)
    print("Se Agregaron los segmentos Loopback :" + str(loopback_ip), "con VRF :"+str(loop_vrf), 'Id de interface asociada a las Loops :'+str(ip_primary))


#----------------------------------------------------------------------------------
def post_id_address(ip_loop):
    nombre_equipo = nb.dcim.devices.get(name=device_name)
    ippp = request_id_ip_address(ip_loop)
    nombre_equipo.primary_ip4 = ippp
    nombre_equipo.save()
    print(f"Actualizando IP Primary del dispositivo {device_name}")

#----------------------------------------------------------------------------------
#fsm_result_3 = display ip interface brief

    # if 'Loop' in ip_loopback_name:
    #     if '10.60.' in ip_loopback_ip:
    #         ip_loopback_name = 'Loop0'
    #         nombre_vrf = 4
    #     else:
    #         ip_loopback_name = 'Loop1'
    #         nombre_vrf = 2

for ww in fsm_result_3:
    ip_loopback_name = ww[0]
    ip_loopback_ip = ww[1]
    if 'Loop' in ip_loopback_name:
        if bool(re.search(r"LoopBack0", ip_loopback_name)) == True:
            ip_loopback_name = 'Loop0'
            ip_loopback_ip = ip_loopback_ip
            name_vrf = 4

        elif bool(re.search(r"LoopBack1", ip_loopback_name)) == True:
            ip_loopback_name = 'Loop1'
            ip_loopback_ip = ip_loopback_ip
            name_vrf = 2

        add_vrf_loopback(ip_loopback_ip, name_vrf, request_interface(ip_loopback_name))

#----------------------------------------------------------------------------------
# for qq in fsm_result_3:
#     ip_loopback_ip = qq[1]
#     if '10.50.' in ip_loopback_ip:
#         post_id_address(ip_loopback_ip)

#----------------------------------------------------------------------------------

# # UPDATE DEVICE (IP PRIMARY)
# def update_device(ip_primary):
#     id_device  = request_devices(device_name)
#     request_url = f"{NB_URL}/api/dcim/devices/?id={device_name}"
#     device_parameters = {
#         "device": id_device,
#         "primary_ip": ip_primary,
#         "primary_ip4": ip_primary,
#     }
#     new_device = requests.post(
#         request_url, headers=HEADERS, json=device_parameters)
#     print("se ha actualizado el dispositivo con IP-Primary: "+str(ip_primary))

# #----------------------------------------------------------------------------------
# # APLICACION AL DISPOSITIVO EL ID DEL IP-PRIMARY
# for rr in fsm_result_3:
#         ip_loopback_name11 = rr[0]
#         ip_loopback_ip11 = rr[1]
#         if 'LoopBack1' in ip_loopback_name11:
#             update_device(request_ip(ip_loopback_ip11))
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#ID DE LA IP ( DEVICE IP)
# def request_ip(id_ip):
#     request_url = f"{NB_URL}/api/ipam/ip-addresses/?address={id_ip}"
#     url_ipaddress = requests.get(request_url, headers=HEADERS)
#     result_ipadress = url_ipaddress.json()
#     for valores_ip in result_ipadress["results"]:
#         return valores_ip["id"]
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------