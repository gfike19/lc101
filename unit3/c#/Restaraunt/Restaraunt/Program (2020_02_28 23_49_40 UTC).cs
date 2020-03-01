using System;
using System.Collections.Generic;

namespace Restaraunt
{
    class Program
    {
        static void Main(string[] args)
        {
            //makes a new MenuItem object following the pattern in MenuItem line 25
            MenuItem turkey = new MenuItem("turkey", "stuffed bird", 10.00, "entree");

            //demonstration of ToString method
            Console.WriteLine(turkey.ToString());

            //instead of doing line 11 many times over, I created objects like this
            //main point is is that a Menu object is filled with a course
            string[] food_stuff = { "dressing", "cranberry sauce", "mashed potatoes" };

            List<MenuItem> thnks_gvng = new List<MenuItem>();
            Random rnd = new Random();

            foreach (string i in food_stuff)
            {
                double price = rnd.NextDouble();
                MenuItem m = new MenuItem(i, "some food", price, "app");
                thnks_gvng.Add(m);
                Menu holiday_specials = new Menu(thnks_gvng);

            }

            //demonstrates the CheckDate method of the MenuItem class, line 65 in MenuItem file
            if (turkey.CheckDate() =="new")
            {
                Console.WriteLine("Spring turkey!!");
            }

            //how you would use the Add and Remove method of the Menu class, lines 29 and 42 in Menu file
            MenuItem green_bean_casserole = new MenuItem("green bean casserole", "tasty", 4.99, "side");
            thnks_gvng.Add(green_bean_casserole);
            thnks_gvng.Remove(green_bean_casserole);

            //used to keep the console screen open until you hit enter
            Console.ReadLine();

        }
    }
}
