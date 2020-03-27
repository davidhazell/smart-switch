# smart-switch


## ABSTRACT

### Improving IoT user experience through on-premises device management #

As power requirements for computation have dropped, the success of Internet of Things (IoT) devices such as smart lights, speakers, and AC sockets have demonstrated a demand for household appliances with increased range of behavioral complexity. Accessing significant marginal functionality of these IoT devices often requires either user expertise or integration with a cloud platform such as Google Assistant or Amazon Alexa. In addition, manufacturer design decisions can lead to common usage patterns that do not mirror expectations about traditional household appliances. For example, users may expect to toggle lights on or off with a switch, but find themselves frustrated due to incompatibility or limited interaction between a physical switch and the digital input and scheduling application. We aim to develop an on-premises IoT management system for Philips Hue smart lighting in which physical and digital state is updated by changes made through either interface. The user can intuitively enable or disable smart lighting with a physical switch, and digitally initiated on/off state change results in equivalent physical switch orientation without cloud service connection. 

## WEEKLY PROGRESS REPORTS

### Week 1

Status Report:
* Purchased and configured switch hardware (RaspberryPi, GPIO board, Soldering Iron, motors, etc)
* Purchased and configured lighting hardware (user account, bridge, lights, etc)
* Demonstrated the ability to use a rotary encoder to get light switch positional data
* Reviewed smart light API documentation
* Reviewed http requests protocol documentation
* Began R&D for smart light API communication

Plan for next week:
* Class definition for switch positional data
* Authenticate with smart light API 
* Global logging configuration

### Week 2

Status report:
* Re-organized project structure into config/test/src directories
* Created class structure for switch positional data
* Started definition global logger configuration for both console and file-based application logging
* Succuessfully authenticated with smart light API

Plan for next week:
* Complete global logging configuration
* Light switch led indicator control
* Control on/off state of single light

### Week 3

Status report:
* Completed global logging configuration
* Light switch LED indicator control

Plan for next week:
* Continued R&D for hardware design
* Communication between hardware devices

### Week 4

Staus report:
* Hardware build: ordered assorted gears
* Wrote test scripts to prove communication between devices (demonstrated switch position controlling led in class)

Plan for next week:
* Continued R&D for hardware design

### Week 5

Status report:
* Hardware build: Installed gears to switch by 1) drilling directly through the pivot point on the plastic light switch 2) inserting a wooden rod through the switch 3) drilling holes in the center of plastic gears 4) fixing gears to wooden rod
* Application is printing switch positional data

Plan for next week:
* Continued R&D for hardware design
* Message queueing system

### Week 6

Plan for next week:
* Hardware build: R&D with motor control including 1) experimenting with different power levels and intervals
* Experimentation with python's queue library.  Built a simple FIFO queue for sending hardware commands to the switch.

Plan for next week:
* Continued R&D for hardware design
* Continued devleopment on message queue system.  Retrieve state updates from switch.

### Week 7

Status report:
* Hardware build: ordered parts to install motors to switch
* Continued development on message queue system. Set up multiple queues for message/reply

Plan for next week:
* Continued R&D for hardware design

### Week 8

Status report:
* Hardware build: conitnued R&D with motor control

Plan for next week:
* Continued R&D for hardware design
* Continued development on message queue system

### Week 9

Status report:
* Hardware build: continued R&D attaching gearing to all devices

Plan for next week:
* Continued R&D for hardware design
* Continued development on message queue system


