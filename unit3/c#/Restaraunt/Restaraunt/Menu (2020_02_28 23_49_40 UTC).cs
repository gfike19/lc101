using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Restaraunt
{
    class Menu
    {
        List<List<MenuItem>> all_courses = new List<List<MenuItem>>();
        //TODO consider: doesn't a menu contain more than one course? How would you set that up? Would a List of Lists be possible?


        private DateTime date = DateTime.Now; //can be used to determine when a menu was made

        //uses a MenuItem's name and 
        Dictionary<string, DateTime> time_stamps = new Dictionary<string, DateTime>();

        public Menu (List<MenuItem> course)
        {
            all_courses.Add(course);
        }

        //TODO consider: Menu is a container for the variable course course is a container for a List of MenuItems why have it set like that?

        public Menu () { } //TODO in what instance would you want to use this rather than line 15?

        //add MenuItem
        public void Add(MenuItem m)
        {
            //adds the item to the private variable course
            course.Add(m);
            //TODO this code is incorrect as this implies we are adding a MenuItem to a Dictionary, which we are refer to line 17
            //time_stamps.Add(m.name(), m.date());
            //date = DateTime.Now();

            //this is correct
            //TODO what is going on here?
            time_stamps[m.GetName()] = DateTime.Now;
        }

        //remove MenuItem
        public void Remove(MenuItem m)
        {
            //TODO this is incorrect, read documentation on what First does to find out why, need to create equals method for MenuItems to implement this
            //course.First(m);
        }

        //TODO A way to print out both a menu item and an entire menu - from studio

        //TODO when was the last MenuItem added? use time_stamps * hint hint *


    }
}
