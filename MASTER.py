#######################################################################################################################
## Medical Products Order and Sales Processing
##  This program processes products and orders and produces sales and build reports.
## 
##  Functions:
##     main
##     f_reference
##     f_test
##     f_menu
##     f_get_products
## 
#######################################################################################################################
## Modules 
import os;
import csv;
import productsmodule


#######################################################################################################################
## Functions
#######################################################################################################################

def f_reference():
    """
    Documentation: Reference function for assignment, operators and operations
    """
    input('\n In f_reference - press any key to continue');
    return  ## End of Function f_reference()  

##=============================================================================
## Main Menu 
##  This function displays the operation menu, gets selection option and enforces the integrity of the selection
##    Display Menu choices
##    Selection choice
##    Validate choice
##  Input: None
##  Output: VALID Menu option selection
##=============================================================================
def f_menu():
## Local variables
    v_option = "";                   ## local menu choice
    t_options = ('1','2', '3', '4', '5', '6', 'r', 't','x','X');   ## List of acceptable options

## Loop on Menu options until a valid option is selected    
    while v_option not in t_options:
        os.system('cls');       ## Clear the screen on windows
        # print("\n" * 50);     ## Clear the screen in IDLE
        
      ## Show menu options        
        print('Select operation')
        print('  1. Load Product List   ')
        print('  2. Load Orders         ')
        print('  3. Process Orders      ')
        print('  4. Display Reports     ')
        print('  5. Process Build Plan  ')
        print('  6. Export Build Plan   ')
        print('  r. Display Referencee  ')
        print('  t. test                ')
        print('  X  Exit                ')
        
        v_option = input('Select option: ') ## Get option selection
        if v_option in t_options : 
            break;  ## Exit if valid selection
        else : 
            print('\nThat is not a valid option');  ## Display error message if not valid option 
            input('Press any key to continue');

    return v_option  ## End of Function f_menu


##=============================================================================
## Get Products 
##  This function loads the product list from the .csv file into a dictionary
##    https://docs.python.org/3.5/library/csv.html
##    Read each line from the file 
##    Append each row into a dictionary 
##    Handle errors (duplicates, empty file)
##    Print dictionary contents for testing
##  Input Parameters: 
##      g_prod_file: .csv products path and filename 
##      p_prod_dict: empty products dictionary
##  Output Results: 
##      g_prod_dict - loaded global products dictionary
##      Process status - Success, Failure
##=============================================================================
def f_get_products():
  ## Local Variables
    v_file    = '';  ## file reference
    v_reader  = '';  ## file reader iterator
    d_row     = {};  ## next row as a dictionary data type
    t_items   = ();  ## tuple to hold each row in the product file
    d_prod    = {};  ## dictionary of tuples to return

  ##  Open the file and set the iterator
    v_file   = open(g_prod_file);       ## Open the file 
    v_reader = csv.DictReader(v_file);  ## Set the file iterator with the first row as the key names. 
                         
 ## Read each row in the file with the values in the first row used as the dictionary keys. 
    for d_row in v_reader:

   ## Get the column values in the row
      t_items = ( d_row['prod_line']
                 ,d_row['desc']
                 ,float(d_row['price'])
                 ,d_row['size']
                 ,d_row['color']
                 ,int(d_row['footprint'])
                );
   ## Update dictionary - Add a key and tuple of product attributes to the products dictionsary
      d_prod[d_row['prod_nbr']] = t_items;

 ## close the file
    v_file.close();

    return d_prod  ## End of Function f_get_products - Return loaded product dictionary


##=============================================================================
## Test
##=============================================================================
def f_test():
    """
    Documentation Test function to prototype various functions
    """
    print ("Inside f_test");
    input();
    return;   ## End of Function f_test


#######################################################################################################################
## MAIN 
##   Program Control Flow
#######################################################################################################################
def main():
  ## =====================
  ## Global Variables
  ## =====================
    global g_prod_file;               ## Declare product file as global
    g_file_path  = os.getcwd(); ## Get current working directory
    print(g_file_path);
    'E:\\PYTHON'
    g_prod_file  = g_file_path + '\\products.csv';  ## product.csv file is in the same directory as the script file  
    
    g_prod_dict     = {};   ## Initialize global products dictionary
    
  ## =====================
  ## Local Variables
  ## =====================
    v_func_status   =  0;   ## Function return status
    v_menu_option   = '';   ## Menu option choice

  ## ==============================================
  ## Process Main Menu option choice
  ## ==============================================
    while v_menu_option not in ['x','X']:
        v_menu_option = f_menu();   ## Disply main menu and get choice
  
    ## ********************************************
    ## Load Product List - option 1
    ## ********************************************
        if  v_menu_option == '1':  
            g_prod_dict   = {};             ## Initialize global products dictionary

      ## Get the product list from the .csv file
            g_prod_dict = f_get_products(); 

      ## Display the contents for the product dictionary until the report is created
            for k, v in g_prod_dict.items(): print(k, v);
            input("press any key to continue");

                            
    ## ********************************************
    ## Load Orders - option 2
    ## ********************************************
        elif v_menu_option == '2':
            print("Load Orders - option 2"); 
            input();
    
    ## ********************************************
    ## Process Orders - option 3
    ## ********************************************
        elif v_menu_option == '3':
            print("Process Orders - option 3"); 
            input();

    ## ********************************************
    ## Display Reports - option 4
    ## ********************************************
        elif v_menu_option == '4':
            print("Display Reports - option 4"); 
            input();

    ## ********************************************
    ## Process Build Plan - option 5
    ## ********************************************
        elif v_menu_option == '5':
            print('Process Build Plan - option 5');
            input();

    ## ********************************************
    ## Export Build Plan - option 6
    ## ********************************************
        elif v_menu_option == '6':
            print('Export Build Plan - option 6');
            input();

    ## ********************************************
    ## Reference
    ## ********************************************
        elif v_menu_option == 'r':
            f_reference();          
            print('Reference - option r');
            print (f_reference.__doc__);
            input();

    ## ********************************************
    ## Test 
    ## ********************************************
        elif v_menu_option == 't':
            f_test();   
            print('Test - option t');
            print (f_test.__doc__);
            input();
           
  ## ********************************************
  ## Exit
  ## ********************************************
        elif v_menu_option.upper() == 'X':
            print('EXITING');
            input();

  ## ********************************************
  ## End of Menu options
  ## ********************************************
        else:                       
            print('ERROR – in main() else - this should never happen');
            input();

    return 0;   # End of Function main()

#######################################################################################################################

## Call main
main();


    
