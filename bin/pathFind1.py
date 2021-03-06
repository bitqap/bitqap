# Python program to print all paths from a source to destination.
# First networkx library is imported
# along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt
import sys

#python2 Documents/qaralama/findPath.py '{"peers": [["161.97.69.136", "194.135.154.14"],["161.97.69.136", "194.135.154.12"],["194.135.154.12", "194.135.154.13"], ["194.135.154.13", "161.97.69.136"]]}'  '161.97.69.136' '161.97.69.136'


from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation
class Graph:
	def __init__(self, vertices):
		# No. of vertices
		self.V = vertices
		# default dictionary to store graph
		self.graph = defaultdict(list)
	# function to add an edge to graph
	
	def addEdge(self, u, v):
		self.graph[u].append(v)
	'''A recursive function to print all paths from 'u' to 'd'.
	visited[] keeps track of vertices in current path.
	path[] stores actual vertices and path_index is current
	index in path[]'''

	def printAllPathsUtil(self, u, d, visited, path):
		# Mark the current node as visited and store in path
		visited[u]= True
		path.append(u)
		# If current vertex is same as destination, then print
		# current path[]
		if u == d:
			print (path)
		else:
			# If current vertex is not destination
			# Recur for all the vertices adjacent to this vertex
			for i in self.graph[u]:
				if visited[i]== False:
					self.printAllPathsUtil(i, d, visited, path)	
		# Remove current vertex from path[] and mark it as unvisited
		path.pop()
		visited[u]= False
	# Prints all paths from 's' to 'd'
	def printAllPaths(self, s, d):
		if d < s:
			# 2(d) < 7(s)
			# tmp=2
			# s=2
			# d=
			tmp=s
			s=d
			d=tmp 
		# Mark all the vertices as not visited
		visited =[False]*(self.V)
		# Create an array to store paths
		path = []
		# Call the recursive helper function to print all paths
		self.printAllPathsUtil(s, d, visited, path)


# Defining a Class (No use. Just in case)
class GraphVisualization:

	def __init__(self):
		
		# visual is a list which stores all
		# the set of edges that constitutes a
		# graph
		self.visual = []
		
	# addEdge function inputs the vertices of an
	# edge and appends it to the visual list
	def addEdge(self, a, b):
		temp = [a, b]
		self.visual.append(temp)
		
	# In visualize function G is an object of
	# class Graph given by networkx G.add_edges_from(visual)
	# creates a graph with a given list
	# nx.draw_networkx(G) - plots the graph
	# plt.show() - displays the graph
	def visualize(self):
		G = nx.Graph()
		G.add_edges_from(self.visual)
		nx.draw_networkx(G)
		plt.show()

# Driver code
#G = GraphVisualization()
#G.addEdge(1, 2)
#G.addEdge(2, 3)
#G.addEdge(3, 4)
#G.addEdge(2, 4)
#G.addEdge(4, 5)
#G.addEdge(5, 6)
#G.addEdge(5, 7)


# Create a graph given in the above diagram
g = Graph(500)
g.addEdge(220, 78)
g.addEdge(82, 95)
g.addEdge(180, 119)
g.addEdge(312, 140)
g.addEdge(461, 352)
g.addEdge(13, 280)
g.addEdge(125, 252)
g.addEdge(180, 374)
g.addEdge(451, 299)
g.addEdge(192, 425)
g.addEdge(270, 370)
g.addEdge(100, 49)
g.addEdge(411, 127)
g.addEdge(91, 402)
g.addEdge(235, 276)
g.addEdge(475, 382)
g.addEdge(438, 283)
g.addEdge(357, 106)
g.addEdge(74, 281)
g.addEdge(171, 298)
g.addEdge(351, 88)
g.addEdge(76, 76)
g.addEdge(151, 429)
g.addEdge(373, 410)
g.addEdge(59, 147)
g.addEdge(153, 348)
g.addEdge(144, 29)
g.addEdge(401, 173)
g.addEdge(254, 22)
g.addEdge(172, 197)
g.addEdge(252, 494)
g.addEdge(345, 179)
g.addEdge(125, 490)
g.addEdge(162, 306)
g.addEdge(293, 483)
g.addEdge(40, 361)
g.addEdge(103, 178)
g.addEdge(461, 151)
g.addEdge(209, 381)
g.addEdge(64, 93)
g.addEdge(264, 351)
g.addEdge(419, 189)
g.addEdge(211, 467)
g.addEdge(490, 361)
g.addEdge(411, 146)
g.addEdge(62, 376)
g.addEdge(339, 350)
g.addEdge(271, 291)
g.addEdge(318, 178)
g.addEdge(239, 261)
g.addEdge(10, 10)
g.addEdge(24, 347)
g.addEdge(81, 410)
g.addEdge(84, 454)
g.addEdge(59, 146)
g.addEdge(431, 166)
g.addEdge(463, 280)
g.addEdge(263, 279)
g.addEdge(171, 345)
g.addEdge(234, 226)
g.addEdge(341, 162)
g.addEdge(149, 425)
g.addEdge(391, 75)
g.addEdge(135, 137)
g.addEdge(378, 422)
g.addEdge(305, 214)
g.addEdge(395, 3)
g.addEdge(444, 121)
g.addEdge(107, 87)
g.addEdge(415, 350)
g.addEdge(382, 8)
g.addEdge(131, 36)
g.addEdge(405, 33)
g.addEdge(235, 454)
g.addEdge(5, 455)
g.addEdge(252, 156)
g.addEdge(172, 487)
g.addEdge(423, 466)
g.addEdge(352, 214)
g.addEdge(28, 338)
g.addEdge(350, 181)
g.addEdge(491, 134)
g.addEdge(17, 70)
g.addEdge(248, 83)
g.addEdge(287, 226)
g.addEdge(479, 378)
g.addEdge(359, 389)
g.addEdge(272, 130)
g.addEdge(500, 216)
g.addEdge(400, 318)
g.addEdge(64, 159)
g.addEdge(167, 355)
g.addEdge(162, 352)
g.addEdge(276, 111)
g.addEdge(450, 204)
g.addEdge(304, 397)
g.addEdge(443, 130)
g.addEdge(286, 414)
g.addEdge(274, 376)
g.addEdge(498, 61)
g.addEdge(398, 305)
g.addEdge(482, 147)
g.addEdge(187, 112)
g.addEdge(443, 77)
g.addEdge(451, 203)
g.addEdge(71, 94)
g.addEdge(67, 162)
g.addEdge(217, 215)
g.addEdge(298, 164)
g.addEdge(257, 374)
g.addEdge(271, 2)
g.addEdge(175, 314)
g.addEdge(398, 298)
g.addEdge(238, 143)
g.addEdge(113, 414)
g.addEdge(271, 92)
g.addEdge(362, 33)
g.addEdge(456, 30)
g.addEdge(474, 351)
g.addEdge(469, 52)
g.addEdge(187, 470)
g.addEdge(201, 405)
g.addEdge(441, 309)
g.addEdge(92, 359)
g.addEdge(302, 423)
g.addEdge(75, 15)
g.addEdge(248, 103)
g.addEdge(266, 47)
g.addEdge(293, 157)
g.addEdge(387, 349)
g.addEdge(66, 147)
g.addEdge(8, 479)
g.addEdge(29, 389)
g.addEdge(468, 371)
g.addEdge(444, 433)
g.addEdge(335, 125)
g.addEdge(292, 280)
g.addEdge(415, 283)
g.addEdge(434, 471)
g.addEdge(87, 387)
g.addEdge(138, 140)
g.addEdge(482, 404)
g.addEdge(135, 385)
g.addEdge(116, 64)
g.addEdge(39, 34)
g.addEdge(92, 118)
g.addEdge(73, 196)
g.addEdge(324, 119)
g.addEdge(79, 151)
g.addEdge(306, 324)
g.addEdge(454, 349)
g.addEdge(155, 111)
g.addEdge(163, 357)
g.addEdge(144, 33)
g.addEdge(87, 303)
g.addEdge(64, 20)
g.addEdge(328, 62)
g.addEdge(131, 315)
g.addEdge(456, 389)
g.addEdge(297, 9)
g.addEdge(344, 458)
g.addEdge(430, 17)
g.addEdge(353, 277)
g.addEdge(470, 396)
g.addEdge(336, 284)
g.addEdge(136, 96)
g.addEdge(486, 12)
g.addEdge(77, 457)
g.addEdge(45, 109)
g.addEdge(310, 59)
g.addEdge(256, 358)
g.addEdge(271, 424)
g.addEdge(447, 470)
g.addEdge(130, 172)
g.addEdge(338, 334)
g.addEdge(488, 146)
g.addEdge(476, 432)
g.addEdge(375, 237)
g.addEdge(116, 212)
g.addEdge(309, 108)
g.addEdge(352, 55)
g.addEdge(432, 225)
g.addEdge(226, 364)
g.addEdge(498, 406)
g.addEdge(466, 154)
g.addEdge(118, 176)
g.addEdge(17, 344)
g.addEdge(96, 56)
g.addEdge(409, 415)
g.addEdge(403, 45)
g.addEdge(5, 47)
g.addEdge(278, 21)
g.addEdge(433, 160)
g.addEdge(481, 381)
g.addEdge(234, 341)
g.addEdge(488, 296)
g.addEdge(197, 44)
g.addEdge(382, 335)
g.addEdge(9, 46)
g.addEdge(382, 216)
g.addEdge(108, 240)
g.addEdge(499, 168)
g.addEdge(40, 196)
g.addEdge(123, 210)
g.addEdge(102, 174)
g.addEdge(103, 435)
g.addEdge(121, 154)
g.addEdge(350, 373)
g.addEdge(154, 364)
g.addEdge(259, 484)
g.addEdge(136, 270)
g.addEdge(204, 82)
g.addEdge(455, 146)
g.addEdge(177, 478)
g.addEdge(181, 335)
g.addEdge(8, 372)
g.addEdge(165, 427)
g.addEdge(345, 166)
g.addEdge(496, 42)
g.addEdge(338, 280)
g.addEdge(276, 169)
g.addEdge(100, 444)
g.addEdge(170, 347)
g.addEdge(244, 457)
g.addEdge(474, 163)
g.addEdge(205, 221)
g.addEdge(206, 285)
g.addEdge(371, 450)
g.addEdge(490, 322)
g.addEdge(392, 417)
g.addEdge(103, 384)
g.addEdge(217, 181)
g.addEdge(283, 299)
g.addEdge(229, 85)
g.addEdge(13, 216)
g.addEdge(425, 442)
g.addEdge(272, 384)
g.addEdge(371, 401)
g.addEdge(333, 394)
g.addEdge(497, 60)
g.addEdge(324, 224)
g.addEdge(75, 38)
g.addEdge(210, 122)
g.addEdge(369, 142)
g.addEdge(415, 147)
g.addEdge(174, 374)
g.addEdge(296, 341)
g.addEdge(173, 332)
g.addEdge(401, 173)
g.addEdge(212, 113)
g.addEdge(280, 238)
g.addEdge(142, 378)
g.addEdge(117, 228)
g.addEdge(398, 5)
g.addEdge(179, 270)
g.addEdge(432, 107)
g.addEdge(470, 138)
g.addEdge(454, 368)
g.addEdge(191, 147)
g.addEdge(371, 365)
g.addEdge(277, 379)
g.addEdge(287, 339)
g.addEdge(486, 73)
g.addEdge(311, 4)
g.addEdge(11, 249)
g.addEdge(190, 46)
g.addEdge(349, 57)
g.addEdge(90, 292)
g.addEdge(93, 38)
g.addEdge(4, 210)
g.addEdge(214, 236)
g.addEdge(463, 381)
g.addEdge(135, 131)
g.addEdge(156, 477)
g.addEdge(107, 411)
g.addEdge(290, 376)
g.addEdge(296, 180)
g.addEdge(254, 271)
g.addEdge(305, 183)
g.addEdge(210, 342)
g.addEdge(127, 34)
g.addEdge(353, 374)
g.addEdge(397, 78)
g.addEdge(3, 24)
g.addEdge(420, 2)
g.addEdge(347, 316)
g.addEdge(353, 179)
g.addEdge(99, 36)
g.addEdge(46, 167)
g.addEdge(431, 33)
g.addEdge(50, 383)
g.addEdge(169, 467)
g.addEdge(384, 77)
g.addEdge(142, 49)
g.addEdge(480, 75)
g.addEdge(75, 99)
g.addEdge(105, 455)
g.addEdge(297, 171)
g.addEdge(336, 395)
g.addEdge(342, 378)
g.addEdge(91, 435)
g.addEdge(385, 141)
g.addEdge(225, 197)
g.addEdge(43, 95)
g.addEdge(289, 113)
g.addEdge(410, 102)
g.addEdge(426, 417)
g.addEdge(353, 360)
g.addEdge(45, 221)
g.addEdge(278, 286)
g.addEdge(399, 86)
g.addEdge(462, 59)
g.addEdge(321, 333)
g.addEdge(237, 163)
g.addEdge(105, 387)
g.addEdge(463, 90)
g.addEdge(178, 155)
g.addEdge(408, 115)
g.addEdge(80, 291)
g.addEdge(124, 416)
g.addEdge(149, 478)
g.addEdge(475, 379)
g.addEdge(137, 99)
g.addEdge(408, 99)
g.addEdge(440, 169)
g.addEdge(55, 377)
g.addEdge(283, 162)
g.addEdge(302, 422)
g.addEdge(141, 339)
g.addEdge(160, 66)
g.addEdge(498, 160)
g.addEdge(309, 293)
g.addEdge(160, 394)
g.addEdge(479, 28)
g.addEdge(113, 83)
g.addEdge(273, 80)
g.addEdge(383, 475)
g.addEdge(185, 385)
g.addEdge(282, 497)
g.addEdge(16, 72)
g.addEdge(338, 335)
g.addEdge(332, 323)
g.addEdge(32, 215)
g.addEdge(309, 76)
g.addEdge(393, 309)
g.addEdge(76, 383)
g.addEdge(182, 271)
g.addEdge(367, 104)
g.addEdge(280, 471)
g.addEdge(303, 229)
g.addEdge(179, 475)
g.addEdge(150, 74)
g.addEdge(311, 116)
g.addEdge(290, 500)
g.addEdge(243, 70)
g.addEdge(253, 487)
g.addEdge(96, 95)
g.addEdge(323, 134)
g.addEdge(368, 11)
g.addEdge(175, 112)
g.addEdge(382, 37)
g.addEdge(180, 85)
g.addEdge(66, 88)
g.addEdge(421, 67)
g.addEdge(174, 486)
g.addEdge(484, 113)
g.addEdge(182, 341)
g.addEdge(229, 434)
g.addEdge(34, 488)
g.addEdge(390, 405)
g.addEdge(387, 428)
g.addEdge(113, 498)
g.addEdge(135, 201)
g.addEdge(264, 30)
g.addEdge(304, 422)
g.addEdge(87, 478)
g.addEdge(385, 251)
g.addEdge(27, 303)
g.addEdge(333, 419)
g.addEdge(79, 52)
g.addEdge(290, 431)
g.addEdge(342, 229)
g.addEdge(84, 29)
g.addEdge(196, 317)
g.addEdge(159, 334)
g.addEdge(104, 135)
g.addEdge(347, 437)
g.addEdge(405, 193)
g.addEdge(366, 165)
g.addEdge(200, 176)
g.addEdge(464, 492)
g.addEdge(74, 216)
g.addEdge(93, 100)
g.addEdge(452, 202)
g.addEdge(160, 18)
g.addEdge(220, 177)
g.addEdge(100, 126)
g.addEdge(346, 5)
g.addEdge(462, 83)
g.addEdge(176, 354)
g.addEdge(467, 416)
g.addEdge(117, 305)
g.addEdge(195, 275)
g.addEdge(23, 438)
g.addEdge(156, 464)
g.addEdge(262, 21)
g.addEdge(287, 452)
g.addEdge(387, 350)
g.addEdge(410, 304)
g.addEdge(356, 225)
g.addEdge(442, 426)
g.addEdge(76, 122)
g.addEdge(325, 66)
g.addEdge(273, 476)
g.addEdge(180, 49)
g.addEdge(327, 264)
g.addEdge(462, 286)
g.addEdge(420, 447)
g.addEdge(104, 158)
g.addEdge(125, 388)
g.addEdge(106, 94)
g.addEdge(351, 255)
g.addEdge(173, 410)
g.addEdge(7, 160)
g.addEdge(64, 363)
g.addEdge(424, 139)
g.addEdge(21, 102)
g.addEdge(287, 1)
g.addEdge(240, 108)
g.addEdge(330, 411)
g.addEdge(99, 459)
g.addEdge(97, 450)
g.addEdge(260, 396)
g.addEdge(133, 221)
g.addEdge(37, 34)
g.addEdge(410, 338)
g.addEdge(149, 122)
g.addEdge(41, 49)
g.addEdge(441, 119)
g.addEdge(321, 163)
g.addEdge(44, 54)
g.addEdge(472, 192)
g.addEdge(62, 399)
g.addEdge(311, 142)
g.addEdge(275, 466)
g.addEdge(223, 322)
g.addEdge(59, 287)
g.addEdge(51, 103)
g.addEdge(116, 57)
g.addEdge(487, 229)
g.addEdge(288, 306)
g.addEdge(282, 52)
g.addEdge(284, 5)
g.addEdge(250, 262)
g.addEdge(457, 6)
g.addEdge(114, 30)
g.addEdge(373, 172)
g.addEdge(233, 166)
g.addEdge(272, 344)
g.addEdge(463, 74)
g.addEdge(273, 261)
g.addEdge(289, 382)
g.addEdge(195, 446)
g.addEdge(231, 85)
g.addEdge(451, 391)
g.addEdge(122, 176)
g.addEdge(367, 51)
g.addEdge(56, 466)
g.addEdge(113, 215)
g.addEdge(301, 428)
g.addEdge(274, 152)
g.addEdge(221, 438)
g.addEdge(349, 472)
g.addEdge(127, 298)
g.addEdge(359, 185)
g.addEdge(358, 415)
g.addEdge(489, 433)
g.addEdge(256, 462)
g.addEdge(383, 313)
g.addEdge(93, 478)
g.addEdge(133, 440)
g.addEdge(97, 263)
g.addEdge(212, 298)
g.addEdge(288, 93)
g.addEdge(447, 98)
g.addEdge(447, 317)
g.addEdge(493, 391)
g.addEdge(273, 415)
g.addEdge(340, 471)
g.addEdge(462, 406)
g.addEdge(306, 48)
g.addEdge(283, 353)
g.addEdge(93, 276)
g.addEdge(63, 158)
g.addEdge(309, 331)
g.addEdge(39, 62)
g.addEdge(81, 249)
g.addEdge(101, 181)
g.addEdge(456, 249)
g.addEdge(246, 371)

s = 101 ; d = 249
print ("Following are all different paths from % d to % d :" %(s, d))
g.printAllPaths(s, d)
#G.visualize()
