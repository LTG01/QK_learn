"""
删除 xml_str 字符串里面多余的空白字符。让文字内容更紧凑输出
"""
import re

xml_str = """
<?xml version="1.0" encoding="UTF-8"?>
<TowerRouteTask>
	

	<FileVer>TowerRouteTask-1.0</FileVer>
	

	<CreateTime>2020-05-09 13:47</CreateTime>
	

	<TaskName>崇玉线_04#</TaskName>
	

	<TowerNum>1</TowerNum>
	

	<PointNum>17</PointNum>
	

	<UseRtk>true</UseRtk>
	

	<TowerRoute>
		

		<LineName>崇玉线</LineName>
		

		<TowerID>04#</TowerID>
		

		<Level>220kV</Level>
		

		<Location>114.6833570,36.5894932</Location>
		

		<Camera>大疆M210 RTK V2+X5S 15mm</Camera>
		

		<PointNum>17</PointNum>
		

		<Point>
			

			<PointID>P03</PointID>
			

			<Latitude>36.589567522511</Latitude>
			

			<Longitude>114.683474283505</Longitude>
			

			<Altitude>82.971476941025</Altitude>
			

			<Yaw>-149,-138,-164,-122,-111,-96</Yaw>
			

			<Pitch>-9,-6,-11,-8,-9,-10</Pitch>
			

			<Angle>22.78,6.60,7.97,5.62,20.29,8.18</Angle>
			

			<Yaw>0</Yaw>
			<Pitch>0</Pitch>
			<type>4</type>
			<id>2</id>
			<variety>0</variety>
			<number>34</number>
			<angle>30</angle>
			<object>11</object>
			<side>A</side>
			<angletype>8</angletype>
			<ZoomPos>33</ZoomPos>
		</Point>

		<Point>
			

			<PointID>P03</PointID>
			

			<Latitude>36.589567522511</Latitude>
			

			<Longitude>114.683474283505</Longitude>
			

			<Altitude>82.971476941025</Altitude>
			

			<Yaw>-149,-138,-164,-122,-111,-96</Yaw>
			

			<Pitch>-9,-6,-11,-8,-9,-10</Pitch>
			

			<Angle>22.78,6.60,7.97,5.62,20.29,8.18</Angle>
			

			<Yaw>0</Yaw>
			<Pitch>0</Pitch>
			<type>4</type>
			<id>2</id>
			<variety>0</variety>
			<number>35</number>
			<angle>30</angle>
			<object>11</object>
			<side>A</side>
			<angletype>8</angletype>
			<ZoomPos>33</ZoomPos>
		</Point>
		
		<Point>
			

			<PointID>P09</PointID>
			

			<Latitude>36.589376059305</Latitude>
			

			<Longitude>114.683264893488</Longitude>
			

			<Altitude>70.170726901929</Altitude>
			

			<Yaw>34,34,34,40,50,60</Yaw>
			

			<Pitch>-7,-13,-19,-4,-6,-7</Pitch>
			

			<Angle>3.81,13.63,4.05,3.79,15.54,4.23</Angle>
			

			<Yaw>0</Yaw>
			<Pitch>0</Pitch>
			<type>4</type>
			<id>2</id>
			<variety>0</variety>
			<number>87</number>
			<angle>30</angle>
			<object>11</object>
			<side>A</side>
			<angletype>8</angletype>
			<ZoomPos>33</ZoomPos>
		</Point>

		<Point>
			

			<PointID>P09</PointID>
			

			<Latitude>36.589376059305</Latitude>
			

			<Longitude>114.683264893488</Longitude>
			

			<Altitude>70.170726901929</Altitude>
			

			<Yaw>34,34,34,40,50,60</Yaw>
			

			<Pitch>-7,-13,-19,-4,-6,-7</Pitch>
			

			<Angle>3.81,13.63,4.05,3.79,15.54,4.23</Angle>
			

			<Yaw>0</Yaw>
			<Pitch>0</Pitch>
			<type>4</type>
			<id>2</id>
			<variety>0</variety>
			<number>88</number>
			<angle>30</angle>
			<object>11</object>
			<side>A</side>
			<angletype>8</angletype>
			<ZoomPos>33</ZoomPos>
		</Point>

		

	</TowerRoute>
	

</TowerRouteTask>


"""
"""在下方实现代码"""
