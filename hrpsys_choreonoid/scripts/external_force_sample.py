import cnoid.Base
import cnoid.BodyPlugin

def addExternalForce(fx=0,fy=0,fz=0,px=0,py=0,pz=0.2,t=0.2,link="WAIST",robot="JAXON_RED"):
    robotname = robot
    linkname = link
    pos   = [px, py, pz] ## link local position
    force = [fx, fy, fz] ## [ N ]
    tm = t ## [ sec ]

    robotItem = cnoid.Base.RootItem.instance().findItem(robotname)
    simulatorItem = cnoid.BodyPlugin.SimulatorItem.findActiveSimulatorItemFor(robotItem)
    pushingLink = robotItem.body().link(linkname)
    if pushingLink:
        simulatorItem.setExternalForce(robotItem, pushingLink, pos, force, tm)
