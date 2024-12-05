import textfsm
import json
from collections import OrderedDict
from pprint import pprint
from netmiko import ConnectHandler, NetMikoAuthenticationException, NetMikoTimeoutException, NetmikoBaseException
from credenciales import user_radius, pass_radius, user_without_radius, pass_without_radius

#print(Connection.find_prompt()[1:-1])

#MODELO DE TARJETAS EN EL ROUTER
def lista_tarjetas(conn_equipo):
    display_elabel_brief = conn_equipo.send_command(f'display elabel brief')
    template_display_elabel_brief = open('templates\huawei_vrp_display_elabel_brief.textfsm')
    display_elabel_brief_table = textfsm.TextFSM(template_display_elabel_brief)
    fsm_result_display_elabel_brief = display_elabel_brief_table.ParseText(display_elabel_brief)

    return fsm_result_display_elabel_brief


#VALIDAR LAS PUERTAS ASOCIADAS A LA TARJETA DEL ROUTER
def lista_puertos(conn_equipo, card):
    display_interface_description_slot_card = conn_equipo.send_command(f'display interface brief GigabitEthernet main | inc 0/{card}/ ')
    template_display_interface_description_slot_card = open('templates\huawei_vrp_display_interface_brief.textfsm')
    display_interface_description_slot_card_table = textfsm.TextFSM(template_display_interface_description_slot_card)
    fsm_result_display_interface_description_slot_card = display_interface_description_slot_card_table.ParseText(display_interface_description_slot_card)

    return fsm_result_display_interface_description_slot_card


#with open('980C_test.txt', 'r') as equipos:
with open('980C.txt', 'r') as equipos:
    device_list = equipos.read().splitlines()

for device in device_list:
    try:
        device_config = {
        "device_type": "huawei_vrpv8",
        "ip":device,
        "username":user_radius,
        "password":pass_radius,
        "global_delay_factor": 10,
        }

        Connection = ConnectHandler(**device_config)
        device_name = Connection.find_prompt()
                    
    except NetMikoAuthenticationException:
            device_config = {
            "device_type": "huawei_vrpv8",
            "ip":device,
            "username":user_without_radius,
            "password":pass_without_radius,
            "global_delay_factor": 10,
            }
            Connection = ConnectHandler(**device_config)
            device_name = Connection.find_prompt()

    cont_libre1010 = 0
    cont_ocupada1010 = 0
    temp_slot21 = []
    cont_libre101 = 0
    cont_ocupada101 = 0

    with open ('1OPTMIZED_ARCHIVO_FINAL_980C.txt','a') as f:  
        card_list = lista_tarjetas(Connection)
        for items in card_list:
            if items[3] == "10x10GE(o)-SFP+":
                lista_final21 = lista_puertos(Connection, items[1])
                for items21 in lista_final21:
                    interface21 = items21[0].split("/")
                    temp_slot21= interface21[2]
                    tarjeta_final21 = interface21[1]
                    if items21[1]  == 'up':
                        escr = f.write((f'{device_name} TARJETA {tarjeta_final21} SLOT: {temp_slot21} MODULO: {items[3]}\t OCUPADA\n'))
                        cont_ocupada1010+=1
                    else:
                        escr = f.write((f'{device_name} TARJETA {tarjeta_final21} SLOT: {temp_slot21} MODULO: {items[3]}\t LIBRE\n'))
                        cont_libre1010+=1
            elif items[3] == "10xGE/FE(o)":
                lista_final22 = lista_puertos(Connection, items[1])
                for items22 in lista_final22:
                    interface22 = items22[0].split("/")
                    temp_slot22 = interface22[2]
                    tarjeta_final22 = interface22[1]
                    if items22[1]  == 'up':
                            escr = f.write((f'{device_name} TARJETA {tarjeta_final22} SLOT: {temp_slot22} MODULO: {items[3]}\t OCUPADA\n'))
                            cont_ocupada101+=1
                    else:
                            escr = f.write((f'{device_name} TARJETA {tarjeta_final22} SLOT: {temp_slot22} MODULO: {items[3]}\t LIBRE\n'))
                            cont_libre101+=1
            
            #print(f'Para el equipo: {device_name} Libres : {cont_libre} Ocupadas : {cont_ocupada}')