def panHome(x, y, z):
    # Get the three coordinates from user
    x_input = input("Enter x coordinate (default 100): ").strip()
    y_input = input("Enter y coordinate (default 200): ").strip()
    z_input = input("Enter z coordinate (default 300): ").strip()

    # Process x coordinate
    if (
        x_input == ""  # First error-exception check
    ):  # If after strip call is blank = no input recieved. inform to use default
        x = 100
        print("No x input. Using default position: 100")
    else:
        try:
            x = int(x_input)  # Second error-exception check
            # Check if input is int/ !NaN by converting to int
            print(f"X position set to: {x}")
        except ValueError:
            x = 100
            print(f"Invalid x input '{x_input}'. Using default position: 100")
            # If number converts to int. Print return input to user

    # Process y coordinate
    if y_input == "":
        y = 200
        print("No y input. Using default position: 200")
    else:
        try:
            y = int(y_input)
            print(f"Y position set to: {y}")
        except ValueError:
            y = 200
            print(f"Invalid y input '{y_input}'. Using default position: 200")

    # Process z coordinate
    if z_input == "":
        z = 300
        print("No z input. Using default position: 300")
    else:
        try:
            z = int(z_input)
            print(f"Z position set to: {z}")
        except ValueError:
            z = 300
            print(f"Invalid z input '{z_input}'. Using default position: 300")

    return x, y, z

    # Print out x, y, z to confirm:
    x, y, z = panHome()
    print(f"\nFinal coordinates: ({x}, {y}, {z})")
