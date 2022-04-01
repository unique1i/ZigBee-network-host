import pyautogui

class serial_param:
    PORT = ""
    BAUD_RATE = 115200


# adjust all gui params here...
class params:
    def __init__(self):
        pass

    hidpi = False
    if pyautogui.size()[0] > 3000:
        hidpi = True
    if hidpi:
        scale = 3
    else:
        scale = 1

    # size of three windows
    main_width = 920 * scale
    main_height = 600 * scale
    logger_width = 520 * scale
    logger_height = 250 * scale
    func_width = 520 * scale
    func_height = 350 * scale
    coord_pos = [20 * scale, 200 * scale]  # int coord pos in the node editor
    discovery_indicator_x_offset = 80 if hidpi == False else 200

    # windows position
    winExitConfirm_pos = [220 * scale, 180 * scale]
    winLog_pos = [400 * scale, 350 * scale]
    winFuncPanel_pos = [400 * scale, 0]
    winWelcome_pos = [250 * scale, 180 * scale]
    winStarted_pos = [50 * scale, 30 * scale]
    winLoadingIndicator_pos = [400 * scale, 200 * scale]

    # colors
    rgb_red = [255, 0, 0]
    rgb_red2 = [195, 67, 100]
    rgb_green = [0, 255, 0]
    rgb_green2 = [255, 179, 13]
    rgb_white = [255, 255, 255]
    rgb_blue = [0,191,255]


    # current command list of host
    command = [["get_device_state","get_power_info"],
               ["set_clock_zero"],
               ["set_all_rgb_colors","set_all_hp_brightness","set_led_programme_effect"],
               ["get_gravity_vector","get_temperature","get_location"]]

    # test
    test_mode = True
    # the maximum payload size for api frame is 255 bytes, we test 6*40 bytes
    groups_payload_test = 9

# coordinator should be named COORD
# adjust all gui params here...
class network:
    def __init__(self):
        pass
    # network
    coord = None         # zigbee coordinator
    xbee_network = None  # class <XBeeNetwork>, represents an XBee Network
    nodes = None         # nodes discovered, list of <remoteXbeeDevice> object
    nodes_id = []        # nodes names, exclude coord
    available_nodes = []  # available nodes of <remoteXbeeDevice>, deal with node add and removal
    available_nodes_id = []
    nodes_obj = []       # list of <node_container> object to save info
    connections = None   # link in the network
    NODE_ID = "NI"

    # logger
    log = None
    last_command_time = None # used for latency test
    latest_latency = 0


class node_container:
    '''
    a wrapper for each node to cover all the info of the floodlight it represents
    '''
    def __init__(self,xbee_obj):
        self.node_xbee = xbee_obj
    # save get_...() response of each node
    node_xbee = None
    is_available = True   # node status, true when init
    temperature = "n/a"   # temperature, use string here
    rssi = float('-inf')  # rssi value foe each node
    led_color = []

    # status check
    handshake_time = None

    # device attribute
    location = []
    device_state = 0
    rgba = []
    brightness = 1
    light_effect =0
    last_msg = [] # when check integrity, used if need to put splitted msg together

# instantiate the <network> object
global net
net = network()