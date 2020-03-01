package robot;

public class robot {
private String name;
private int x_pos;
private int y_pos;
private int speed;
private String dir;

public robot (String name, int x_pos, int y_pos, int speed, String dir) {
//	this.name =  "";
//	this.x_pos =  0;
//	this.y_pos  = 0;
//	this.speed = 0;
//	this.dir  = "";
	
	public String getName () {
		return this.name;
	}

}

public static String move (x_pos, y_pos, speed, dir) {
	dir = dir.equalsIgnoreCase(dir);
	
	switch(dir) {
	case north:
		y_pos = (y_pos + 1) * speed;
	case south: 
		y_pos = (y_pos - 1) * speed;
	case east:
		x_pos = (x_pos + 1) * speed;
	case west:
		x_pos = (x_pos - 1) * speed;
}
	return (x_pos + "" + y_pos);
}

public static String rotate(boolean rot) {
	dir = dir.equalsIgnoreCase(dir);
	String dir_list [] = {
			"north", "east", "south", "west"
	};
	if(rot == true) {
		String current_dir = dir_list.find(dir);
		dir = current_dir +1;
	} return dir;
}

public static int calcDist () {
	return dist;
}


}
