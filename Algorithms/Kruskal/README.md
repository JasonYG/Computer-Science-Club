# Kruskal's Algorithm

Kruskal's algorithm is used to find the minimum-spanning-tree (MST) of a connected and undirected graph. It is a greedy algorithm and has a time complexity of O(E log E) or O(E log V), where E and V are the number of edges and vertices in the graph, respectively. It is implemented with the disjoint-set data structure.

- **CCC** - Usually [S4](https://dmoj.ca/problems/?search=S4&show_types=1&category=4) and [S5](https://dmoj.ca/problems/?search=S5&show_types=1&category=4) problems, on undirected graphs
- **Skills** - Classes and Interfaces, [Disjoint-Set](https://en.wikipedia.org/wiki/Disjoint_sets) data structure, Graphs

## Table of contents
- [Minimum-spanning-tree (MST)](#Minimum-spanning-tree)
- [Story time!](#Story)
- [Setup](#Setup)
- [Algorithm](#Algorithm)
- [Testing the code](#Testing-the-code)
- [Full source code](#Source-code)
- [Practice](#Practice)


---

## Minimum spanning tree
A minimum-spanning-tree (MST) connects all the vertices in a graph together without any cycles and with the smallest possible total edge weight (hence the minimum in the name).

<img src="mst_comparison.jpg" width="800">

*Image: HackerEarth Minimum Spanning Tree*

---

## Story
Immediately after exiting the time machine you are greeted with the sound of thunder and heavy rain. Amidst the darkness you discover you've landed in ancient China. You spot a small village not far away from your machine and set out to find shelter (the time machine conducts electricity). Upon entering the village, you discover that there are no roads connecting the various buildings and found yourself becoming fatigued as the muddy ground caused you to sink every step you took. Having finally made it into one of the houses, you are unexpectedly greeted by the leader of the village. Unable to explain your situation and where you came from, you decided to quickly change the conversation to the lack of roads in the village. The mayor pitied you and offered to build roads for the village provided that you must come up with a plan to ensure:
- all buildings in the village are connected together by a road, directly or indirectly
- the lowest cost of paving the roads.

Each road costs a different amount so how can you come up with a plan to save the village money and solve their problem of having no roads?

<img src="story.png" width="800">

*Image: The University of Texas at Dallas, Sergey Bereg: Minimum Spanning Tree*

---

## Setup
Before we begin Kruskal's algorithm, we need to create a class for the Edges in our tree.

Let's think of what we need in this Edge class:
- beginning vertex
- ending vertex
- weight (cost)

The **beginning vertex (bv)** connects to the **ending vertex (ev)** and forms an **edge with a weight (cost)**.

<img src="Kruskal_1.png" width="500">

In the image above, we observe that for any edge, there is a beginning vertex, ending vertex and weight.

*Ex.* 
> bv = 0; ev = 1; cost = 4;

We see that **vertex 0** is connected to **vertex 1** with an edge of **cost 4**. With context, one could say that to build a road between city 0 and city 1, it would cost $4.

---

Because Kruskal's algorithm is a greedy algorithm, it takes the immediate lowest edge weight and adds it to the MST provided that the new edge does not form a cycle in the MST. We can sort the edges by weight from lowest to highest.

Great, now we understand the graph, we can create the Edge class!

---
First, let's create a class called **Edge** and implement the *Comparable* interface so we can call a **.sort()** later on our array of **Edge**. In this class, we have 3 variables: **bv**, **ev** and **cost**. These help define which two vertices an **Edge** connects to and the weight of the **Edge**.

```Java
public static class Edge implements Comparable<Edge> {
    //beginning vertex, ending vertex, weight of edge
    int bv; int ev; int cost;

    //Empty constructor
    public Edge() {
        //to initialize arrays later
    }

    //Full constructor
    public Edge(int bv, int ev, int cost) {
        this.bv = bv;
        this.ev = ev;
        this.cost = cost;
    }
}
```

Next we will need to create a method for our *Comparable* interface so that we can call a **.sort()** later. How the **compareTo** method works is that it compares the **Edges** by subtracting the **cost** of 2 **Edges** and a negative value (< 0) means that the other **Edge** has a higher cost than this **Edge**, a positive value (> 0) means that the other **Edge** has a higher cost than this **Edge** and zero (0) means that the two **Edges** have the same cost.

```Java
@Override
public int compareTo(Edge other) {
    return this.cost - other.cost;
}
```

Here's another way to implement the same method, doing the same thing as described above.

```Java
@Override
public int compareTo(Edge o) {
    if (o.cost > this.cost) {
        return -1;
    } else if (this.cost > o.cost) {
        return 1;
    } else {
        return 0;
    }
}
```

Now it's time to add some of the things we need to store our **Edges** and other stuff related to the MST.

Go ahead and add these variables into your main class:

```Java
int V; int E; //Number of vertices and edges in the graph
Edge[] edge; Edge[] mst; //Array of Edge holds the entire graph and mst array holds the Edges that are in the mst
int[] parent; //Disjoint-set
int[] size; //Size array for size of set
```

It's time to create our *constructor* for the **Main** class. This is where we initialize all of our arrays we defined in the code sample above. We make use of the **empty** *constructor* when we initialize the **Edge** array and the MST array. We also need to set each element in the disjoint-set array (parent) to -1 because we assume -1 is the root/parent (which is true since each vertex is not connected to anything right now, so itself is its root/parent). Then set each element in the **size** array to 1 because all the vertices are unconnected so they're in their own set, therefore the size is 1.

```Java
public Main (int v, int e) {
    V = v; E = e;

    edge = new Edge[e];
    for (int i = 0; i < e; i++) {
        edge[i] = new Edge();
    }

    mst = new Edge[v-1];
    for (int i = 0; i < v - 1; i++) {
        mst[i] = new Edge();
    }

    parent = new int[v];
    for (int i = 0; i < v; i++) {
        parent[i] = -1;
    }

    size = new int[v];
    for (int i = 0; i < v; i++) {
        size[i] = 1;
    }
}
```

Now we need to create two functions for our disjoint-set: *union* and *find*. The *union* function connects two vertices together and the *find* function the root/parent of the vertex. These two functions are commonly used together as Kruskal's algorithm will *find* the root/parent of the beginning vertex and ending vertex, then using *union* to join their root/parent together.

```Java
public static int find(int v) {
    if (parent[v] == -1) { // if -1 it is the root/parent
        return v; //the vertex is already the parent
    } else {
        return find(parent[v]); //if it's not the parent, keep using find to find the parent
    }
}
```

```Java
public static void union(int bv, int ev) {
    int pb = find(bv); //parent of beginning vertex
    int pe = find(ev); //parent of beginning vertex

    if (size[pb] < size[pe]) { //if the size of one set is greater than the other
        /* 
        * set the parent of the smaller set to the parent of the larger set, 
        * we're attaching the ENTIRE smaller set from its parent vertex to 
        * the parent vertex of the larger set.
        */
        parent[pb] = pe;
        /*
        * add the size of the smaller set to the size of the
        * larger set (since they're 1 set now)
        */
        size[pe] += size[pb];
    } else {
        //same procedure as above
        parent[pe] = pb;
        size[pb] += size[pe];
    }
}
```

Hooray! We're finally done setting up all the classes and functions we need to implement Kruskal's algorithm and now we can start doing cool things in the **main** function to use the algorithm.

---

## Algorithm
Remember the [time](#Story) you convinced a mayor in ancient China to build roads for his village? Well, let's see how you can do exactly that before being trapped in the year 2001 B.C. forever.

The village architect gives you an estimate (a very accurate estimate) of the cost to build roads between buildings, she presents to you the following map:

<img src="village_graph.png" width="500">

From the map, you quickly write down the vertices and edges information in the following format:

| Road #  | Beginning Vertex  | Ending Vertex  | Cost  |
|---|---|---|---|
| 0  | 0 | 1  | 3  |
| 1  | 0  | 5  | 10  |
| 2  | 0  | 7  | 6  |
| 3  | 1  | 4  | 2  |
| 4  | 1  | 2  | 5  |
| 5  | 2  | 3  | 4  |
| 6  | 2  | 8  | 9  |
| 7  | 3  | 4  | 8  |
| 8  | 3  | 8  | 7  |
| 9  | 5  | 6  | 1  |
| 10  | 6  | 7  | 7  |
| 11  | 6  | 8  | 100  |
| 12  | 2  | 7  | 1  |

You note that the order of the beginning vertex and ending vertex doesn't matter since there's nothing stopping you from going from house A to house B and back from house B to house A.

To transfer the table to code, you can store it into the **Edge[] edge** we created earlier.

```Java
//Create a Scanner so we can input the information about edges
Scanner sc = new Scanner(System.in);

//Let's input how many vertices and edges we're given
int v = sc.nextInt(); int e = sc.nextInt();

//Create a new object of your Main class, let's call it "graph"
//and pass in the parameters v (vertices) and e (edges)
//The constructor of the Main class will initialize all our
//arrays for us.
Main graph = new Main(v, e);

//Using a for-loop, input the information about each edge
for (int i = 0; i < e; i++) {
    int bv = sc.nextInt(); //beginning vertex
    int ev = sc.nextInt(); //ending vertex
    int cost = sc.nextInt();
    //Now let's use the 2nd constructor of the Edge class
    //and put the above information into our Edge array
    graph.edge[i] = new Edge(bv, ev, cost);
}
```

Then you sort the roads from least cost to greatest cost:

```Java
//Using Arrays.sort(), we make use of the Comparable interface
//we implemented in the Edge class
Arrays.sort(graph.edge);
```

| Road #  | Beginning Vertex  | Ending Vertex  | Cost  |
|---|---|---|---|
| 12  | 2  | 7  | 1  |
| 9  | 5  | 6  | 1  |
| 3  | 1  | 4  | 2  |
| 0  | 0 | 1  | 3  |
| 5  | 2  | 3  | 4  |
| 4  | 1  | 2  | 5  |
| 2  | 0  | 7  | 6  |
| 10  | 6  | 7  | 7  |
| 8  | 3  | 8  | 7  |
| 7  | 3  | 4  | 8  |
| 6  | 2  | 8  | 9  |
| 1  | 0  | 5  | 10  |
| 11  | 6  | 8  | 100  |


Note that there might be roads that have the same cost, that's OK, just make sure the roads as a whole is in ascending order.

---

Alright, here's when Kruskal's algorithm **REALLY** begins, it's a greedy algorithm so it's going to act **greedy**. We're going to pick the road that costs the least to build, and conveniently, that's the one at the top of the list! Also, **the number of edges in a MST is the number of vertices in the graph minus one** (for example, if a graph has 10 vertices, then the MST will have 9 edges). Therefore we know we're done when we have 1 less edge than vertices in our MST.

> **Road #12**, *I Choose You!*

Now you check if adding this road to the MST will create a **cycle**. In other words, if adding the road will form a loop in a graph. Since this is our first road in the MST, it obviously doesn't form a **cycle**, so we're safe to add it.

<img src="village_step1.png" width="300">

Looks like we have a lot more roads to check, so we have to keep going. Let's look at our table and pick the next cheapest road to build.

> **Road #19**, *Lookin' good*

<img src="village_step2.png" width="300">

There are 9 vertices in this graph, so we need 8 edges in our MST. We only have 2 so far, 6 more to go!

> **Road #3**, *Very nice*

<img src="village_step3.png" width="300">

I think you get the idea: check table for the next lowest cost edge, make sure it doesn't form a cycle when added to the MST, if it does, DO NOT add it.

<img src="village_step4.png" width="300">

Looks good so far, we haven't encountered a cycle yet.

<img src="village_step5.png" width="300">

**Road #4** does not form a cycle, so we can add it to the MST.

<img src="village_step6.png" width="300">

Uh oh, **Road #2** forms a cycle when we add it to the MST! We must remove it!

<img src="village_step7.png" width="300">

Much better, we've removed **Road #2** from the MST and added **Road #10** that doesn't form a cycle.

<img src="village_step8.png" width="300">

Ok, we are done our MST because all the vertices are connected!

<img src="village_step9.png" width="300">

---

Here's the code to implement Kruskal's algorithm (on the same graph as shown in the pictures):

```Java
//Create a count variable to keep track of the edges we've added
int count = 0;
//Create a for-loop to loop through all the given edges
//we sorted earlier
for (int i = 0; i < e; i++) {
    //Grab the details of the ith edge
    //it should be the edge with the least cost
    int bv = graph.edge[i].bv;
    int ev = graph.edge[i].ev;
    int cost = graph.edge[i].cost;

    //Using the find function we created earlier
    //for our disjoint-set, use it to find bv's root/parent
    //and ev's root/parent. Store in respective variables
    int pb = graph.find(bv); //parent of beginning vertex
    int pe = graph.find(ev); //parent of ending vertex

    //If the parent of bv and ev are not the same,
    //then the edge won't form a cycle
    if (pb != pe) {
        //Using the union function
        graph.union(bv, ev);

        //Add the edge to the MST array
        //Using count because not every given edge (i)
        //can be added to the MST
        graph.mst[count].bv = bv;
        graph.mst[count].ev = ev;
        graph.mst[count].cost = cost;

        //If the MST has V - 1 edges in it
        //then we have found the MST of the graph
        //WE'VE COMPLETED THE ALGORITHM!
        if (count == v - 1) {
            break;
        }
    }
}
```

And if you want to see the completed MST:

```Java
for (int i = 0; i < v - 1; i++) {
    System.out.print(graph.mst[i].bv + " ");
    System.out.print(graph.mst[i].ev + " ");
    System.out.println(graph.mst[i].cost);
}
```

---

## Testing the code
From the section earlier, you learned how Kruskal's algorithm works and how to implement it with code. Now it's time to validate our work and see if we can successfully obtain a MST from the map give by the architect.

**Input**

The first line of input will contain **V**, the amount of vertices and **E**, the amount of edges.
The next **E** lines will contain the beginning vertex, ending vertex and cost of the *i*-th edge.

```
9 13
0 1 3
0 5 10
0 7 6
1 4 2
1 2 5
2 3 4
2 8 9
3 4 8
3 8 7
5 6 1
6 7 7
6 8 100
2 7 1
```

**Output**

```
5 6 1
2 7 1
1 4 2
0 1 3
2 3 4
1 2 5
3 8 7
6 7 7
```

Checking with our completed graph we can see that our program outputs the correct MST:

<img src="village_step9.png" width="300">

---

## Souce code
Feel free to check out the full source code [here](KruskalLesson.java).

---

## Practice
Here are some problems for you to practice Kruskal's algorithm. If you need help, feel free to contact us at the [JFSS Computer Science Club Slack channel](https://jfss-compsci.slack.com/).

**Easy**
- [Disjoint Set Test](#https://dmoj.ca/problem/ds2)
- [Line Graph](#https://dmoj.ca/problem/dmopc15c6p4)

**Medium**
- [Trucking Troubles](#https://dmoj.ca/problem/ccc03s5)

**Hard**
- [Minimum Cost Flow](#https://dmoj.ca/problem/ccc17s4)

*More problems will be added; for up to date information and extra practice please contact us on Slack.*

---
