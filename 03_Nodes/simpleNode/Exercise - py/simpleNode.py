# Copyright (C) 
# 
# Author: Autodesk Developer Network

#For this exercise, search for the TODO keywords and follow the instructions in
#comments. If you are unsure of what you need to do, feel free to ask the instructor
#or look into the solution folder.
#Each #... line is a line of code you need to write or complete.

import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import sys

#- Assing a unique node ID to your new node class.
#- Ask ADN or Autodesk product support to reserve IDs for your company. You can
#- reserve ID by block of 64, 128, 256, or 512 consecutive ID.
#-
#- In the solution project, 0x00001 is a temporary ID reserved for development. Never use that ID in a
#- production environment.

kPluginNodeTypeName = "simpleNode"
#- TODO: Define here your unique node ID
simpleNodeId = #...

# Node definition
class simpleNode(OpenMayaMPx.MPxNode):
	# Node attributes
	input = OpenMaya.MObject()
	#- TODO: Declare here the output attribute
	#- TODO: ...
	
	def __init__(self):
		OpenMayaMPx.MPxNode.__init__(self)
		
	#- This method computes the value of the given output plug based
	#- on the values of the input attributes.
	#- Arguments:
	#- 	plug - the plug to compute
	#- 	data - object that provides access to the attributes for this node
	def compute(self,plug,dataBlock):
		if ( plug == simpleNode.output ):
			#- Get a handle to the input attribute that we will need for the
			#- computation. If the value is being supplied via a connection 
			#- in the dependency graph, then this call will cause all upstream  
			#- connections to be evaluated so that the correct value is supplied.
			inputData = dataBlock.inputValue( simpleNode.input )
			
			#- Read the input value from the handle.
			result = inputData.asFloat()

			#- Get a handle to the output attribute. This is similar to the
			#- "inputValue" call above except that no dependency graph 
			#- computation will be done as a result of this call.

			#- Get a handle on the aOutput attribute
			outputHandle = dataBlock.outputValue( simpleNode.output )

			#- TODO: Set the new output value to the handle (multiply the value by 2 for
			#- example to see a change [result * 2])
			#...

			#- Mark the destination plug as being clean. This will prevent the
			#- dependency graph from repeating this calculation until an input 
			#- attribute of this node which affects this output attribute changes.

			#- TODO: Tell Maya the plug is now clean
			#...

		#- Tell Maya that we do not know how to handle this plug, but let give a chance
		#- to our parent class to evaluate it.
		return OpenMaya.kUnknownParameter

# Creator
def nodeCreator():
	return OpenMayaMPx.asMPxPtr( simpleNode() )

#- The initialize method is called to create and initialize all of the 
#- attributes and attribute dependencies for this node type. This is 
#- only called once when the node type is registered with Maya.
#-
def nodeInitializer():
	#- Initialize a float input attribute using the MFnNumericAttribute
	#- class. Make that attribute definition saved into Maya file (setStorable),
	#- and selectable in the channel box (setKeyable).

	#- Create a generic attribute using MFnNumericAttribute
	nAttr = OpenMaya.MFnNumericAttribute()
	simpleNode.input = nAttr.create( "input", "in", OpenMaya.MFnNumericData.kFloat, 0.0 )
	#- Attribute will be written to files when this type of node is stored
 	nAttr.setStorable(1)
	#- Attribute is keyable and will show up in the channel box
 	nAttr.setKeyable(1)

	#- TODO: Initialize a float output attribute using the MFnNumericAttribute
	#- class. Make that attribute definition not saved into Maya file.
	#...
	#- TODO: Attribute will not be written to files when this type of node is stored
	#...
	

	#- Now add the attribute to your node definition using the addAttribute()
	#- method.

	#- Add the attributes we have created to the node
	simpleNode.addAttribute( simpleNode.input )
	#- TODO: Add the output attribute to the node type definition
	#...
	
	
	#- Finally tell Maya how the information should flow through your node.
	#- This will also tell Maya how the dirty flag is propagated in your node
	#- and ultimatelly in the Maya DG. To do this, use the attributeAffects()
	#- method to link your node' attributes together.

	#- TODO: Set up a dependency between the input and the output. This will cause
	#- the output to be marked dirty when the input changes. The output will
	#- then be recomputed the next time the value of the output is requested.
	#...

# Initialize the script plug-in
def initializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject)
	try:
		#- TODO: Register your node here, so Maya can use it and recognize it
		#- TODO: while reading/saving a file which has instance of this node type.
		#...
	except:
		sys.stderr.write( "Failed to register node: %s" % kPluginNodeTypeName )
		raise

# Uninitialize the script plug-in
def uninitializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject)
	try:
		#- TODO: Unregister your node here, so Maya stops using it.
		#...
	except:
		sys.stderr.write( "Failed to deregister node: %s" % kPluginNodeTypeName )
		raise