import java.util.ArrayList;

class recursivePathFinding {
    static int[][] directions = {
        {-1, 0}, //up
        {0, 1}, // right
        {1, 0}, //down
        {0, -1} //left
    };

    //5 parameters
    //maze - 2d string array representing maze
    //wall - character representing a wall
    //curr - the current co-ords
    //end - defines the end of the maze in co-ords
    //seen - 2d array representing maps but with True and False
    //path - current path the recursive algorithm has traversed
    public static boolean walk(String[][] maze, String wall, Point curr,
    Point end, Boolean[][] seen, ArrayList<Point> path)
    {
        //Base Cases
        //1. out of bounds
        if(curr.x < 0 || curr.x >= maze[0].length
        || curr.y < 0 || curr.y >= maze.length)
        {
            return false;
        }

        //2. hit a wall
        if(maze[curr.y][curr.x] == wall)
        {
            return false;
        }

        //3. already seen this block
        if(seen[curr.y][curr.x] == true)
        {
            return false;
        }

        //4. it is the end
        if(curr.x == end.x && curr.y == end.y)
        {
            path.add(curr);
            return true;
        }

        //adding this block to the seen blocks so we don't look over it again
        seen[curr.y][curr.x] = true;

        path.add(curr);
        //walk
        for(int i = 0; i < directions.length; i++)
        {
            Point next_curr = new Point(curr.x + directions[i][0], curr.y + directions[i][1]);
            Boolean succ = walk(maze, "X", next_curr, end, seen, path);
            if(succ == true)
            {
                return true;
            }
        }
        return false;
    }


    public static void printPath(ArrayList<Point> path)
    {
        for(int i = 0; i < path.size(); i++)
        {
            path.get(i).print();
        }
    }
    public static void main(String[] args)
    {
        String[][] maze = {
            {"X", "X", "X", "X", " ", "X"},
            {"X", "X", "X", "X", " ", "X"},
            {"X", "X", " ", " ", " ", "X"},
            {"X", "X", " ", "X", "X", "X"}
        };
        Point start = new Point(4, 0);
        Point end = new Point(2, 3);
        Boolean[][] seen = new Boolean[maze.length][maze[0].length];
        
        //populating the seen array with falses
        for(int i = 0; i < seen.length; i++)
        {
            for(int j = 0; j < seen[0].length; j++)
            {
                seen[i][j] = false;
            }
        }
        ArrayList<Point> path = new ArrayList<Point>();
        walk(maze, "X", start, end, seen, path);
        printPath(path);

    }
}
