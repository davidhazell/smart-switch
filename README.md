# smart-switch

############
# ABSTRACT #
############

# Improving IoT user experience through on-premises device management #

As power requirements for computation have dropped, the success of Internet of Things (IoT) devices such as smart lights, speakers, and AC sockets have demonstrated a demand for household appliances with increased range of behavioral complexity. Accessing significant marginal functionality of these IoT devices often requires either user expertise or integration with a cloud platform such as Google Assistant or Amazon Alexa. In addition, manufacturer design decisions can lead to common usage patterns that do not mirror expectations about traditional household appliances. For example, users may expect to toggle lights on or off with a switch, but find themselves frustrated due to incompatibility or limited interaction between a physical switch and the digital input and scheduling application. We aim to develop an on-premises IoT management system for Philips Hue smart lighting in which physical and digital state is updated by changes made through either interface. The user can intuitively enable or disable smart lighting with a physical switch, and digitally initiated on/off state change results in equivalent physical switch orientation without cloud service connection. 

########################### 
# WEEKLY PROGRESS REPORTS #
###########################

# Week 1 #

Status Report:
* Purchased and configured switch hardware (RaspberryPi, GPIO board, Soldering Iron, motors, etc)
* Purchased and configured lighting hardware (user account, bridge, lights, etc)
* Demonstrated the ability to use a rotary encoder to get light switch positional data
* Reviewed smart light API documentation
* Reviewed http requests protocol documentation
* Began R&D for smart light API communication

Plan for next week:
* Class definition for switch positional data
* Led indication of switch state (on/off, green/red)
* Brushless motor control (for physical movement of switch)
* Authenticate with smart light API 
* Present sample light API requests and responses
