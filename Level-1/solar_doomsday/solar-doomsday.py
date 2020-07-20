import math

def solution(area):
	if(area <= 0 or area > 1000000):
		raise Exception("Area given is out of bounds");
	panelDims = []
	while(area > 0):
		nextPanelSize = math.floor(math.sqrt(area)) * math.floor(math.sqrt(area));
		panelDims.append(nextPanelSize);
		area -= nextPanelSize;
	return panelDims