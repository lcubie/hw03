"""
Name: Lina
Peers: No collarborators
References: I lookes up syntax for or conditionals and I reviewed the python tutor functions in context link from the slideshow
"""

# imported modules
import statistics # let's us use mean, median, mode

# This is a global variable (seen by all local scopes)
grades = [0,0,0,0,0] # initialized with five zeros

# Task 1:
#  Complete the function "read_five_ints" below:
def read_five_ints():
    
    """ updates content of grades depending on the user's input """
    for idx in range ( len(grades) ):
       
        in_str=input("Give me the grade in [0,10]:");
        
        #verifies that it is a digit
        if in_str.isdigit() == False:
            print("Error in read_five_ints: input string is not for an integer")
            exit()
        
        #if it is a digit, transforms the input into a integer, places it in the grades list 
        else:
            in_str = int(in_str)
            grades[idx] = in_str
        
        #Checks that the integer is within the defined range(by our input text NOT a variable")    
        if in_str > 10 or in_str < 0:
            print("Error in read_five_ints: input integer outside of range")
            exit()
                
    


# Task 2:
#  Complete the function "pick_averaging_method" below:
def pick_averaging_method():
    """ returns an average depending on the user's selection """
    method = input("Pick 'a' for mean, 'b' for median, 'c' for mode: ");
    
    #Based on the input, tells the used what it chose and calculates the avg return through the chosen method
    if method == "a":
        print("picked: Mean");
        avg = statistics.mean(grades);
    
    elif method == "b":
        print("picked: Median");
        avg = statistics.median(grades);
    
    elif method == "c":
        print("picked: Mode");
        avg = statistics.mode(grades);
    
    #If something outside of the expected "a", "b", or "c" input (as described by the input text) it will return and error message and end the code
    else:
        print("Error in pick_averaging_method: incorrect option picked");
        exit()
    #returns the variable avg for pick visualization to use    
    return avg

# Task 3:
#  Complete the function "pick_visualization" below:
def pick_visualization(average):
    """ prints the result in a format that depends on the user's selection"""
    
    vis = input("Pick '1' for print average, or '2' for plot average: ");
    
    # Calls different functions based on the chosen "1" or "2" and if neither chosen returns an error and ends the code
    if vis=="1":
        print_list_and_average(average);
    elif vis=="2":
        plot_grades(average);
    else:
        print("Error in pick_visualization: incorrect option picked")
        exit()


# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

# Do not modify this function
def print_list_and_average(average):
    print(f"The average of {grades} is {average}")

def plot_grades(average):
    print ("Annotated grades: ")
    prev = -1
    for g in grades:
        if prev < average < g:
            print("^", end="")
        if average > g:
            print(" ", end="")
        if average == g:
            print(f"({g})", end="")
        else:
            print(f"{g} ", end="")
        prev = g
    print()

# Do not modify this function
def main ():
    # calls the function and updates the grades
    read_five_ints()
    # this reorders the values in grades in increasing order
    grades.sort()
    print(f"Sorted grades: {grades}")
    # gets avg depending on selection
    avg = pick_averaging_method()
    # prints or 'plots' result
    pick_visualization(avg)
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
