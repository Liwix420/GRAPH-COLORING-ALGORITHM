def main():
    import functions

    while(True):
        print("CHOOSE OPTION: \n1. Read graph from file\n2. Generate graph")
        choice = int(input(": "))
        if choice == 1:
            file_name = "dane.txt"
            edges = functions.read_file(file_name)
            break
        elif choice == 2:
            n = int(input("Enter number of vertices: "))
            d = float(input("Enter density of your graph (0-1): "))
            edges = functions.generate_graph(n,d)
            break
        else:
            print("There is no such an option!")

    neighbours = functions.create_list_of_neighbours(edges)

    colors = functions.color_graph(neighbours)

    print("ALL EDGES: \n",edges)
    print("NEIGHBOURS OF EACH VERTEX: \n",neighbours)
    print("COLOR OF EACH VERTEX: \n",colors)
    print("COLORS AND ALL THEIR VERTICES: ")
    functions.print_color_vertices(colors)

if __name__ == "__main__":
    main()